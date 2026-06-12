# 💬 Multilingual Customer Support Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink)
![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-6A0DAD?style=for-the-badge)

**A RAG-powered customer support chatbot that detects your language and replies in the same language — automatically.**

[🚀 Live Demo](https://multilingual-rag-bot-ipmj9skgpeg9ssges92pxk.streamlit.app/) · [⚙️ Setup](#️-local-setup)

</div>

---

## ✨ Features

- 🌐 **11 Languages in UI** — English, Hindi, Spanish, French, German, Arabic, Bengali, Tamil, Telugu, Chinese, Japanese
- 🔍 **Auto Language Detection** — Write in any language, bot replies in the same language
- 🤖 **RAG Pipeline** — Answers only from your FAQ data, zero hallucinations
- ⚡ **Groq LLaMA 3.3 70B** — Super fast responses
- 🧠 **Multilingual Embeddings** — Semantic search works across 50+ languages
- 🗑️ **Clear Chat Button** — Reset conversation anytime from sidebar

---

## 🏗️ How It Works

```
User types question (any language)
            ↓
Multilingual Embedding Model
paraphrase-multilingual-MiniLM-L12-v2
            ↓
ChromaDB finds Top 3 matching FAQ chunks
            ↓
Groq LLaMA 3.3 70B reads context
+ detects language of question
+ replies in same language
            ↓
Answer in user's language ✅
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| 🖥️ Frontend | Streamlit |
| 🔗 RAG Pipeline | LangChain |
| 🧠 LLM | Groq — LLaMA 3.3 70B Versatile |
| 📦 Vector Database | ChromaDB |
| 🌍 Embeddings | paraphrase-multilingual-MiniLM-L12-v2 |
| 🔐 Environment | python-dotenv |

---

## 📁 Project Structure

```
multilingual-rag-bot/
├── data/
│   └── faq.txt          ← Your FAQ knowledge base
├── app.py               ← Streamlit UI + language switcher
├── rag_chain.py         ← RAG pipeline + multilingual prompt
├── ingest.py            ← Chunks + embeds + saves to ChromaDB
├── requirements.txt     ← All dependencies
├── .gitignore           ← Keeps .env and chroma_db private
└── README.md
```

---

## ⚙️ Local Setup

**Requirements:** Python 3.10+ and a free Groq API key from [console.groq.com](https://console.groq.com)

**1. Clone the repo**
```bash
git clone https://github.com/bhardwajrenuka94/Multilingual-rag-bot.git
cd Multilingual-rag-bot
```

**2. Create and activate virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create .env file and add your Groq API key**
```
GROQ_API_KEY=your_actual_key_here
```

**5. Build the vector database**
```bash
python ingest.py
```

**6. Run the app**
```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser ✅

---

## 🌐 Supported UI Languages

| # | Language | Script |
|---|----------|--------|
| 1 | English | Latin |
| 2 | Hindi | Devanagari |
| 3 | Spanish | Latin |
| 4 | French | Latin |
| 5 | German | Latin |
| 6 | Arabic | Arabic |
| 7 | Bengali | Bengali |
| 8 | Tamil | Tamil |
| 9 | Telugu | Telugu |
| 10 | Chinese | Hanzi |
| 11 | Japanese | Hiragana / Katakana |

The embedding model supports 50+ languages — users can type in any language even if it's not in the UI dropdown.

---

## ☁️ Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://multilingual-rag-bot-ipmj9skgpeg9ssges92pxk.streamlit.app/)
3. Connect your GitHub repo
4. Set **Main file path** → `app.py`
5. Go to **Settings → Secrets** and add:
```
GROQ_API_KEY = "your_actual_key_here"
```
6. Click **Deploy** 🚀

---

## 🔒 Security Note

`.env` and `chroma_db/` are listed in `.gitignore` so your API key and local vector data are never pushed to GitHub.

---

## 👩‍💻 Author

**Renuka Bhardwaj**

[![GitHub](https://img.shields.io/badge/GitHub-bhardwajrenuka94-181717?style=flat&logo=github)](https://github.com/bhardwajrenuka94)

---

<div align="center">
⭐ Found this useful? Give it a star!
</div>
