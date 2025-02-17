from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

def vectorizar(texto):
    vector = vectorizer.fit_transform(texto)
    palabras = vectorizer.get_feature_names_out()
    return vector.toarray(), palabras