from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score

# Datos de ejemplo (textos y categorías)
texts = ["el gato está en el tejado", "el perro corre rápido", "gato y perro son amigos"]
labels = [0, 1, 1]  # 0 = gato, 1 = perro

# Vectorizar los textos
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.33, random_state=42)

# Entrenar un clasificador
model = MultinomialNB()
model.fit(X_train, y_train)

# Predecir sobre los datos de prueba
y_pred = model.predict(X_test)

# Ver la precisión del modelo
print("Precisión:", accuracy_score(y_test, y_pred))