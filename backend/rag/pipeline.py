from backend.rag.loader import load_pdf
from backend.rag.splitter import split_docs
from backend.rag.embeddings import get_embeddings
from backend.rag.vectorstore import create_vectorstore
from backend.rag.retriever import get_retriever
from backend.rag.chain import build_chain
from backend.rag.prompt import get_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.chat_models import ChatOllama
# from langchain_community.llms import HuggingFaceEndpoint
# from langchain_openai import ChatOpenAI
from langsmith import traceable
from dotenv import load_dotenv
load_dotenv()
import os

if not os.getenv("GOOGLE_API_KEY"):
    raise RuntimeError("GOOGLE_API_KEY is not set")



class Ragpipeline:
    def __init__(self, pdf_bytes: bytes):
        docs =load_pdf(pdf_bytes)
        chunks = split_docs(docs)
        embeddings = get_embeddings()
        db = create_vectorstore(chunks, embeddings)
        retriever = get_retriever(db)
        prompt = get_prompt()
        # llm = ChatOpenAI(model = "gpt-4o")
        llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
        # llm = ChatOllama(model = "mistral:latest", num_gpu = 0)
        # llm = HuggingFaceEndpoint(
        #     repo_id="google/flan-t5-base",
        #     task="text2text-generation",
        # #     model_kwargs={
        # #     "temperature": 0.2,
        # #     "max_length": 512
        # # })

        self.chain = build_chain(retriever, prompt, llm)
    @traceable(name = "ask_fn")
    def ask(self, question : str) -> str:
        return self.chain.invoke(question)
