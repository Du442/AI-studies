import os
from dotenv import load_dotenv

# PDF Documents Loader
from langchain_community.document_loaders import PyPDFLoader

# Text divider in squares
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Embeddings and LLM
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# Vetorial DB
from langchain_community.vectorstores import Chroma

# RAG Chain
from langchain_classic.chains import retrieval_qa

load_dotenv(override=True)

# Path to file
path = "regras_futebol.pdf"

# Load the PDF
loader = PyPDFLoader(path)
documents = loader.load()

# Quantity of pages loaded.
print(len(documents))

# Split the documents in less chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

# Initialize Embeddings
embeddings = OpenAIEmbeddings(
    model="text-embeddings-3-small",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Create Vetorial DB
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_regras_futebol"
)

# Create Retriever
retriever = vectorstore.as_retriever(
    search_type="similiarity",
    search_kwargs={"k": 3}
)

# Initialize model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Create RAG chain
qa_chain = retrieval_qa.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)