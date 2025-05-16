# 📄 DocuQuery – Smart Document Q&A Chatbot

DocuQuery is an AI-powered chatbot that allows users to interact with documents by uploading them and asking questions directly. It supports various file formats, uses large language models (LLMs) for intelligent answers, and presents everything in a ChatGPT-style interface.

---

## 🚀 Features

- 📎 Upload PDF, DOCX, or TXT files  
- ✨ Summarize uploaded documents  
- 🧠 Extract key entities using NLP  
- 💬 Ask questions and get real-time answers  
- 🔁 Retains full chat history during session  
- 👥 Secure Sign Up / Sign In system  
- 📊 Select between LLM models (LLaMA, Bart, etc.)  
- 🎨 Clean ChatGPT-like user interface

---

## 🧰 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **NLP/LLMs**: LangChain, LLaMA, Bart  
- **Vector Store**: FAISS  
- **Document Parsing**: PyMuPDF, python-docx, textract  
- **Auth**: Basic JSON file-based  
- **Deployment**: Streamlit Cloud / Local

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/dakshgoti14/DocuQuery.git
cd DocuQuery
```
### 2. Create & Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```
---

### 📁 Project Structure
```bash
DocuQuery/
│
├── app.py                      # Main Streamlit app
├── requirements.txt
├── README.md
├── data/
│   └── users.json              # User credentials
├── utils/
│   ├── summarizer.py           # Document summarization logic
│   ├── ner.py                  # Named entity recognition
│   ├── qa_engine.py            # Vector store & QA logic
│   ├── file_handler.py         # File parsing methods
│   └── auth.py                 # Auth functions
```
### 🌐 Deployment Guide
#### Deploy to Streamlit Cloud (Free)
  - 1. Push your project to GitHub
  - 2. Go to https://streamlit.io/cloud
  - 3. Click "New App" → Select your GitHub repo and branch
  - 4. Set app.py as the entry file
  - 5. Click Deploy

⚠️ Important: Do NOT commit your venv/ folder. It should be excluded via .gitignore.

🛠 Tips for GitHub
If you get this error:

arduino
Copy
Edit
remote: error: File ... exceeds GitHub’s file size limit
Run:

bash
Copy
Edit
git rm -r --cached venv/
echo "venv/" >> .gitignore
Then recommit and push:

bash
Copy
Edit
git add .
git commit -m "Clean up venv"
git push origin main
📌 Future Roadmap
🌍 OAuth or Google login

🧾 Multi-document support

📤 Export chat history

🧠 Add support for OpenAI, Claude, Mistral

🖼️ Document content visualization

🤝 Contributing
Fork this repo

Create a new branch (git checkout -b feature-name)

Make your changes

Commit and push (git push origin feature-name)

Open a pull request

📄 License
MIT License – free to use and modify for personal or commercial use.

👨‍💻 Author
Daksh Goti
GitHub: @dakshgoti14
Feel free to connect or contribute!

yaml
Copy
Edit

---

Let me know if you'd like to:

- Add a demo video or GIF  
- Add badges (e.g. Python version, license)  
- Auto-deploy to Streamlit Cloud with a one-click badge






