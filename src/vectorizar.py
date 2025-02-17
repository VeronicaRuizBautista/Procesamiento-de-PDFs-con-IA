from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

def vectorizar(textos):
    if isinstance(textos, str):
        textos = [textos]  # Convertir a lista si es una sola cadena
    
    vector = vectorizer.fit_transform(textos)
    palabras = vectorizer.get_feature_names_out()
    
    return vector.toarray(), palabras