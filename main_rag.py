from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from conn_model import ai

embeddings = OpenAIEmbeddings()

model = ai()

files = [
    "documents/GTB_gold_Nov23.pdf",
    "documents/GTB_platinum_Nov23.pdf",
    "documents/GTB_standard_Nov23.pdf"
]

documents = sum(
    [
        PyPDFLoader(file).load() for file in files
    ], []
)
document = TextLoader(
    "documents/GTB_gold_Nov23.txt",
    encoding="utf-8"
).load()

pieces = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=100
).split_documents(document)

data_recovery = FAISS.from_documents(
    pieces, embeddings
).as_retriever(search_kwargs={"k":2})

secure_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Answer with the provided content"),
        ("human", "{query}\n\n Context: \n{context}\n\nResponse:")
    ]
)

chain = secure_prompt | model | StrOutputParser()

def answer(question:str):
    node = data_recovery.invoke(question)
    context = "\n\n".join(a_node.page_content for a_node in pieces)
    return chain.invoke(
        {
            "query": question, "context": context
        }
    )

print(answer("How can i proceed if a item had stolen?"))