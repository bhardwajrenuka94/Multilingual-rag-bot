import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

# ── Multilingual embedding model ──────────────────────────────────────────────
# paraphrase-multilingual-MiniLM-L12-v2 supports 50+ languages natively,
# including Hindi, Arabic, Chinese, Japanese, Tamil, Telugu, Bengali, etc.
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# ── Vector store ──────────────────────────────────────────────────────────────
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# ── LLM ───────────────────────────────────────────────────────────────────────
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

# ── Prompt template ───────────────────────────────────────────────────────────
# The prompt explicitly instructs the LLM to:
#   1. Detect the language of the customer question.
#   2. Reply in that same language.
#   3. Only use information from the retrieved context.
MULTILINGUAL_PROMPT = PromptTemplate.from_template("""
You are a helpful and polite customer support assistant that serves users worldwide.

IMPORTANT LANGUAGE RULE:
- Detect the language in which the customer has written their question.
- Always respond in that SAME language.
- If the question is in Hindi, answer in Hindi.
- If the question is in Spanish, answer in Spanish.
- If the question is in French, answer in French.
- If the question is in Tamil, answer in Tamil.
- If the question is in Telugu, answer in Telugu.
- If the question is in Bengali, answer in Bengali.
- If the question is in Arabic, answer in Arabic (right-to-left is fine).
- If the question is in Chinese, answer in Chinese.
- If the question is in Japanese, answer in Japanese.
- For any other language detected, reply in that same language.
- Only fall back to English if the language cannot be determined.

ANSWER RULE:
Use ONLY the information provided in the context below to answer the question.
If the answer is not in the context, say the equivalent of:
"I don't have information about that. Please contact our support team directly."
— but say it in the SAME language as the question.

Context:
{context}

Customer Question: {question}

Your Answer (in the same language as the question):
""")

# ── Helpers ───────────────────────────────────────────────────────────────────
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_chain(interface_language: str = "English"):
    """
    Returns a RAG chain.
    `interface_language` is currently accepted for future customisation
    (e.g. logging, analytics) but the LLM auto-detects reply language
    from the question itself, so callers can simply pass the UI language.
    """
    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | MULTILINGUAL_PROMPT
        | llm
        | StrOutputParser()
    )
    return chain


# ── Convenience default export (backward-compatible) ─────────────────────────
chain = get_chain()