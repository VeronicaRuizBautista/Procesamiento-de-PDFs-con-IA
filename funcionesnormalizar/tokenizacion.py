from nltk.tokenize import word_tokenize
import nltk
import re

nltk.download('punkt_tab')

def tokenizar(texto):
    texto_limpio = re.sub(r"[^a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]", "", texto) 
    tokens = word_tokenize(texto_limpio)
    return tokens