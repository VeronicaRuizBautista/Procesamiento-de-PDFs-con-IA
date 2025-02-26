from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import streamlit as st

def clasificar(vector, textos):
    n_clusters = 5
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(vector)
    labels = kmeans.labels_
    
    vector_train, vector_test, labels_train, labels_test, textos_train, textos_test = train_test_split(vector, labels, textos, test_size=0.33, random_state=42)
    
    model = GaussianNB()
    model.fit(vector_train, labels_train)
    
    y_pred = model.predict(vector_test)
    # Mostrar cómo clasificó cada frase
    classification_results = []
    for texto, prediccion in zip(textos_test, y_pred):
        texto = " ".join(texto)
        classification_results.append(f"Frase: {texto}\nClase predicha: {prediccion}\n---")
        
    return accuracy_score(labels_test, y_pred), classification_results
    