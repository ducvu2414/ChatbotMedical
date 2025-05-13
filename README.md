## 🛠️ Cài đặt môi trường

### 1. Tạo Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

## 🔐 Tạo file `.env`

Tạo tệp `.env` trong thư mục gốc với nội dung:

```dotenv
GROQ_API_KEY="your_groq_api_key_here"
PINECONE_API_KEY="your_pinecone_api_key_here"
```
---

## 🔄 Đồng bộ dữ liệu lên Pinecone

```bash
python src/ingest.py
```

---

## 🚀 Chạy chatbot

```bash
streamlit run app.py
```

---

## 📌 Tài liệu tham khảo

- [LangChain Docs](https://docs.langchain.com/)
- [Pinecone Docs](https://docs.pinecone.io/)
- [Streamlit Docs](https://docs.streamlit.io/)

---

Nếu bạn thấy dự án này hữu ích, hãy ⭐️ hoặc chia sẻ nhé!  
Mọi thắc mắc vui lòng liên hệ hoặc mở issue.
