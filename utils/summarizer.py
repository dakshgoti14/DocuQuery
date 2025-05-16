from transformers import pipeline

# Initialize the summarizer pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to summarize the text
def summarize_text(text):
    if not text:
        raise ValueError("The provided text is empty or invalid.")
    
    # Use the summarizer to generate the summary
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']
