# 🤖 Hybrid AI Tutor Chatbot

A Hybrid AI Tutor Chatbot built using Google's Gemini API and Retrieval-Augmented Generation (RAG).

## Features

- 📄 Chat with PDF documents
- 🤖 General AI Chat using Gemini
- 🧠 Conversation Memory
- 🔍 FAISS Vector Search
- 📚 RAG Pipeline
- 📝 PDF Text Extraction
- ⚡ Configurable Generation Parameters
- 🛡 Error Handling

## Tech Stack

- Python
- Google Gemini API
- FAISS
- NumPy
- pdfplumber
- LangChain Text Splitter

## Project Structure

```
AI Chatbot
│
├── utils
├── data
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Tutor-Chatbot.git
```

Go inside the folder

```bash
cd AI-Tutor-Chatbot
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the chatbot

```bash
python app.py
```

## Current Features

- Hybrid Chatbot
- RAG
- Memory
- FAISS
- PDF Question Answering

## Future Improvements

- Tool Calling
- AI Agent
- Streamlit Interface
- Image Understanding
- Deployment