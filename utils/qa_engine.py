from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM  # if you still want to use LLaMA
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Define available models
MODELS = {
    "LLaMA": OllamaLLM(model="llama3"),
    "Bart": ChatOpenAI(model="facebook/bart-large-cnn")  # Replace with actual supported type if needed
}

# Function to create vector store from text
def create_vector_store(text):
    if not text or not isinstance(text, str):
        raise ValueError("The provided text is invalid or empty.")
    splitter = CharacterTextSplitter()
    texts = splitter.split_text(text)
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_texts(texts, embeddings)
    return db

# Function to create a Q&A chain based on selected model
def create_qa_chain(vector_store, model_name="LLaMA"):
    # Select model based on user preference
    llm = MODELS.get(model_name, MODELS["LLaMA"])  # Default to GPT-3.5 if model is not found
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return qa_chain
