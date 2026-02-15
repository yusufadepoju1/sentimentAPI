import re
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

STOPWORDS = {
    "the","is","and","to","a","of","in","it","that","this","was","for","on",
    "are","with","as","i","you","he","she","they","we","be","been","have","has",
    "at","by","an","or","from","but","not","my","your","our","their"
}

def preprocess_review(text: str) -> str:
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()
    words = text.split()
    words = [ps.stem(w) for w in words if w not in STOPWORDS]
    return " ".join(words)
