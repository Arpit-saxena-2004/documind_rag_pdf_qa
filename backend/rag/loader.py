from pypdf import PdfReader
from langchain_core.documents import Document
from langsmith import traceable
import io

@traceable(name="load_pdf_fn")
def load_pdf(pdf_bytes: bytes):
    reader = PdfReader(io.BytesIO(pdf_bytes))
    docs = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            docs.append(Document(page_content=text))

    return docs