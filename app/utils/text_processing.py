import spacy

nlp = spacy.load("ja_core_news_sm")

def tokenize_text(text):
    doc = nlp(text)
    return [token.text for token in doc]

def extract_nouns(text):
    doc = nlp(text)
    return [token.text for token in doc if token.pos_ == "NOUN"]
