# URL-RAG

A Python application that converts web URLs to PDF documents and performs Retrieval-Augmented Generation (RAG) queries on the content using LlamaIndex.

## Overview

URL-RAG is a workflow-based application that:
1. Takes a web URL as input
2. Converts the web page to a PDF document using Playwright
3. Creates a vector index from the PDF content using LlamaIndex
4. Performs RAG queries to extract detailed step-by-step information from the content

## Features

- **URL to PDF Conversion**: Automatically converts web pages to PDF format
- **Vector Indexing**: Creates searchable vector embeddings from PDF content
- **RAG Queries**: Performs intelligent queries to extract structured information
- **Workflow-based Architecture**: Uses LlamaIndex workflows for clean, modular processing
- **Structured Output**: Returns results as structured step-by-step content

## Installation

### Prerequisites

- Python 3.13+
- Poetry (for dependency management)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd url-rag
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Install Playwright browsers:
```bash
poetry run playwright install chromium
```

## Usage

### Basic Usage

Run the application with a URL as an argument:

```bash
poetry run python url_rag/app.py "https://example.com"
```

### Example

```bash
poetry run python url_rag/app.py "https://docs.python.org/3/tutorial/"
```

This will:
1. Convert the Python tutorial page to PDF
2. Create a vector index from the content
3. Query the content for detailed step-by-step information
4. Display the results

## Project Structure

```
url-rag/
├── url_rag/
│   ├── __init__.py
│   ├── app.py                 # Main application and workflow
│   ├── rag_service.py        # RAG service for indexing and querying
│   ├── url_to_pdf_service.py # URL to PDF conversion service
│   └── constants.py          # Application constants
├── data/                     # Directory for generated PDFs
├── tests/                    # Test files
├── pyproject.toml           # Poetry configuration
└── README.md               # This file
```

## Architecture

The application uses a workflow-based architecture with the following steps:

1. **Input Reception**: Receives URL and query parameters
2. **URL to PDF**: Converts the web page to PDF using Playwright
3. **PDF Indexing**: Creates a vector index from the PDF content
4. **RAG Query**: Performs intelligent queries on the indexed content

### Key Components

- **UrlRagWorkflow**: Main workflow orchestrating the entire process
- **RagService**: Handles vector indexing and querying using LlamaIndex
- **URLToPdfService**: Converts web pages to PDF using Playwright
- **Event Classes**: Define the data flow between workflow steps

## Dependencies

- **llama-index**: For RAG functionality and vector indexing
- **playwright**: For web page to PDF conversion
- **pydantic**: For data validation and structured output

## Configuration

The application uses the following configuration:

- **Input Directory**: `data/` (configurable in `constants.py`)
- **PDF Format**: A4, portrait orientation
- **Query Engine**: LlamaIndex VectorStoreIndex with structured output

## Output Format

The application returns structured content as an array of steps:

```python
class Step(BaseModel):
    content: str

class Content(BaseModel):
    steps: List[Step]
```

## Development

### Running Tests

```bash
poetry run pytest tests/
```

### Code Style

The project follows Python best practices and uses type hints throughout.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Author

**Anwesh Mishra**  
Email: anweshthecool0@gmail.com

## Troubleshooting

### Common Issues

1. **Playwright Installation**: Make sure to run `poetry run playwright install chromium` after installing dependencies
2. **PDF Generation**: Ensure the target URL is accessible and doesn't require authentication
3. **Memory Issues**: Large web pages may require more memory for PDF conversion

### Support

For issues and questions, please open an issue on the repository or contact the author.
