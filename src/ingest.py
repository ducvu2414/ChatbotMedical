import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from helper import load_pdf_file, text_split, download_hugging_face_embeddings

load_dotenv()

PDF_FOLDER_PATH = "Data"

documents = load_pdf_file(PDF_FOLDER_PATH)
text_chunks = text_split(documents)
print(f"✅ Đã tách {len(text_chunks)} đoạn văn bản từ PDF.")

embeddings = download_hugging_face_embeddings()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
index_name = "medicalbot"
pc = Pinecone(api_key=PINECONE_API_KEY)

if index_name in [i['name'] for i in pc.list_indexes()]:
    print(f"⚠️ Đang xóa index cũ '{index_name}' do sai kích thước dimension...")
    pc.delete_index(index_name)
    print(f"✅ Đã xóa index '{index_name}'.")

spec = ServerlessSpec(cloud="aws", region="us-east-1")
pc.create_index(name=index_name, dimension=384, metric="cosine", spec=spec)
print(f"✅ Index '{index_name}' đã được tạo với dimension=384.")

index = pc.Index(index_name)

vector_store = PineconeVectorStore(index=index, embedding=embeddings)
vector_store.add_documents(text_chunks)

print("✅ Đã đẩy dữ liệu PDF lên Pinecone thành công.")