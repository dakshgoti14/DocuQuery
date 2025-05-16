# utils/nlp_utils.py
import spacy
from transformers import pipeline

# Load spaCy model for NER
nlp = spacy.load("en_core_web_sm")

# Load Hugging Face pipeline for summarization
summarizer = pipeline("summarization")

def summarize_document(text):
    # Summarize the document using Hugging Face summarizer
    summary = summarizer(text, max_length=300, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def extract_entities(text):
    # Use spaCy for Named Entity Recognition (NER)
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
