import gensim
from gensim.models import Word2Vec
import numpy as np

def vectorizar(textos):
    model = Word2Vec(sentences = textos, min_count=1, window=5, workers=4)
    palabras = list(model.wv.index_to_key)
    texto_vectorizado = np.array([model.wv[palabra] for palabra in palabras])
    vector = np.mean([model.wv[palabra] for palabra in palabras], axis=0)
    return texto_vectorizado, palabras, vector

from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer("all-MiniLM-L6-v2")

def vectorizar_parrafo(textos):
    texto_vectorizado = modelo.encode(textos)
    return texto_vectorizado