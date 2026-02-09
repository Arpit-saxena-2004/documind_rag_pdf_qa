from langchain_core.prompts import PromptTemplate
from langsmith import traceable

@traceable(name="get_prompt_fn")
def get_prompt():
    return PromptTemplate(
        template="""You are a helpful assistant that answers questions based on provided documents.

Instructions:
- Answer based ONLY on the information provided in the context below
- Be accurate and specific when the context supports it
- If the context doesn't contain enough information to answer the question, say "I don't have enough information in the provided context to answer this question"
- If the user is greeting you, respond in a friendly manner

Context:
{context}

Question: {question}

Answer:""",
        input_variables=["context", "question"]
    )
