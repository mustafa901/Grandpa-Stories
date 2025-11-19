import re

def extract_highlights(text):
    sentences = re.split(r"[.!؟]", text)
    important = [s.strip() for s in sentences if any(word in s for word in [
        "تذكر", "أهم", "مرة", "قصة", "حدث", "يوم", "كنت", "تعلم"
    ])]
    
    return important[:6]
