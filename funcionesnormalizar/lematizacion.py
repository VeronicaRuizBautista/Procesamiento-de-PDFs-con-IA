from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()


def lematizar(tokens):
    lemas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemas