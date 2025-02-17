from funcionesnormalizar.tokenizacion import tokenizar
from funcionesnormalizar.lematizacion import lematizar
from nltk.tokenize import sent_tokenize
import nltk

def normalizar(texto):
    oraciones= sent_tokenize(texto)
    oraciones_normalizadas =[]
    for oracion in oraciones:   
        tokens = tokenizar(oracion)
        lemas = lematizar(tokens)
        oraciones_normalizadas.append(lemas)
    return oraciones_normalizadas