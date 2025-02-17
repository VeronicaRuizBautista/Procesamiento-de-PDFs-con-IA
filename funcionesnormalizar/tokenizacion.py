from nltk.tokenize import word_tokenize
import nltk
import re

nltk.download('punkt_tab')

def tokenizar(texto):
    texto_limpio = re.sub(r"[^a-zA-Z\s]", "", texto.lower())
    tokens = word_tokenize(texto_limpio)
    return tokens