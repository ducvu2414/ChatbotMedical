import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

load_dotenv()

# embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medicalbot"
index = pc.Index(index_name)
vector_store = PineconeVectorStore(index=index, embedding=embeddings)


def search_db(user_query: str) -> list:
    if user_query.strip() != "":
        sim_docs =[]
        result = vector_store.similarity_search_with_score(
        user_query, k=3
        )
        for doc in result:
            sim_docs.append(doc[0].page_content)
        
        return sim_docs  
    else:
        return []  

