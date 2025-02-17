from funcionesnormalizar.tokenizacion import tokenizar
from funcionesnormalizar.lematizacion import lematizar

def normalizar(texto):
    tokens = tokenizar(texto)
    lemas = lematizar(tokens)
    return lemas