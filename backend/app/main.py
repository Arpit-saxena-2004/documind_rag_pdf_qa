from fastapi import FastAPI
from backend.app.routes import router
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI(title="PDF Q&A Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for local dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
