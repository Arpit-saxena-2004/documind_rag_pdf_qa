from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda
)
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
@traceable(name="build_chain_fn")
def build_chain(retriever, prompt, llm):
    parallel = RunnableParallel({
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    })

    return parallel | prompt | llm | StrOutputParser()
