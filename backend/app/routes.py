from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from backend.rag.pipeline import Ragpipeline

router = APIRouter()
pipeline = None  # in-memory, per process


class Question(BaseModel):
    question: str


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global pipeline

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    pdf_bytes = await file.read()

    pipeline = Ragpipeline(pdf_bytes)

    return {"message": "PDF uploaded and processed"}


@router.post("/ask")
async def ask_question(payload: Question):
    if pipeline is None:
        raise HTTPException(status_code=400, detail="Upload a PDF first")

    return {"answer": pipeline.ask(payload.question)}