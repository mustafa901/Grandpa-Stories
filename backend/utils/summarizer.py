from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="marefa-nlp/marefa-mt5-small-arabic-summarization"
)

def summarize_text(text):
    out = summarizer(text, max_length=120, min_length=40)
    return out[0]["summary_text"]
