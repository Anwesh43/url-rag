from llama_index.core.workflow import Workflow, Event, StartEvent, StopEvent, step
from rag_service import RagService
from url_to_pdf_service import URLToPdfService
import datetime
import os
from constants import INPUT_DIR
import asyncio
import sys
from dotenv import load_dotenv

load_dotenv()

ragService = RagService(INPUT_DIR)


class UrlToPdfEvent(Event):
    inputUrl: str
    query: str


class PDFToIndexEvent(Event):
    query: str
    inputFile: str


class RagQueryEvent(Event):
    query: str


class UrlRagWorkflow(Workflow):

    @step
    def receiveInput(self, event: StartEvent) -> UrlToPdfEvent:
        os.makedirs(INPUT_DIR, exist_ok=True)
        print("Created directory")
        return UrlToPdfEvent(inputUrl=event.topic, query=event.query)

    @step
    def urlToPdf(self, event: UrlToPdfEvent) -> PDFToIndexEvent:
        now = int(datetime.datetime.utcnow().timestamp())
        URLToPdfService.urlToPdf(
            url=event.inputUrl, input=f"{INPUT_DIR}/url_{now}.pdf")

        print(f"Created pdf {INPUT_DIR}/url_{now}.pdf")
        return PDFToIndexEvent(query=event.query, inputFile=f"{INPUT_DIR}/url_{now}.pdf")

    @step
    def pdfToIndex(self, event: PDFToIndexEvent) -> RagQueryEvent:
        # if not (ragService.index_created):

        # ragService.add_document(INPUT_DIR)
        ragService.create_index()
        print("Created index")
        return RagQueryEvent(query=event.query)

    @step
    def ragQuery(self, event: RagQueryEvent) -> StopEvent:
        result = ragService.query(event.query)
        print(result.steps)
        return StopEvent(result=result.steps)


async def main(url: str):
    ragFlow = UrlRagWorkflow()
    steps = await ragFlow.run(topic=url, query="Give detailed description in each step as an array of Step")
    print(steps)
    i = 0
    for step in steps:
        print(f"In step {i}")
        print(step.content)
        i = i + 1
if __name__ == "__main__":
    if len(sys.argv) == 2:
        asyncio.run(main(sys.argv[1]))
    else:
        print("Please give url")
