from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from pydantic import BaseModel
import os
from typing import List


class Step(BaseModel):
    content: str


class Content(BaseModel):
    steps: List[Step]


class RagService:
    def __init__(self, folder: str):
        self.folder = folder
        self.index_created = False

    def create_index(self):
        reader = SimpleDirectoryReader(input_dir=self.folder)
        self.index = VectorStoreIndex.from_documents(reader.load_data())
        self.engine = self.index.as_query_engine(output_cls=Content)
        self.index_created = True

    def add_document(self, input_folder):
        reader = SimpleDirectoryReader(input_dir=input_folder)
        self.index.insert(reader.load_data())

    def query(self, queryStr: str):
        return self.engine.query(queryStr)
