from nltk.stem import wordNetLematizer
import nltk

nltk.download('wordnet')

lematizer = wordNetLematizer()


def lematizar(tokens):
    lemas = [lematizer.lemmatize(tokens) for token in tokens]
    return lemas