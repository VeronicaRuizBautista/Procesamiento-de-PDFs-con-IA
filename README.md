# Procesamiento de PDF con IA: extracción, vectorización e integración de chatbots 📜🤖

Este proyecto permite extraer, normalizar y vectorizar información de archivos PDF, tanto digitales como escaneados, utilizando Word2Vec para generar embeddings semánticamente ricos del texto. Los embeddings generados se almacenan en una base de datos vectorial Qdrant, lo que facilita la recuperación de información similar de manera eficiente. Además, el sistema cuenta con un chatbot basado en el modelo generativo TinyLlama/TinyLlama-1.1B-Chat-v1.0, el cual responde preguntas sobre el contenido del PDF, utilizando los embeddings para obtener contexto relevante y generar respuestas precisas y coherentes. El proyecto también incluye herramientas para clasificar el contenido utilizando KMeans y Multinomial Naive Bayes, y ofrece una visualización interactiva a través de Streamlit. Además, se han añadido los archivos necesarios para empaquetar el proyecto en un contenedor Docker y orquestarlo con Kubernetes, facilitando su despliegue y escalabilidad en entornos distribuidos.

🔹 **Características principales** 

- ✅ Extracción de texto y tablas de PDFs digitales y escaneados.
- ✅ Normalización del texto con **NLTK**: eliminación de signos de puntuación, stopwords y lematización.
- ✅ Vectorización del texto usando **Word2Vec**, mejorando la representación semántica de los textos.
- ✅ Almacenamiento de los embeddings generados en la base vectorial **Qdrant** para una recuperación eficiente de información.
- ✅ Implementación de un **chatbot generativo** utilizando **TinyLlama/TinyLlama-1.1B-Chat-v1.0** que responde preguntas relacionadas con el contenido de los PDFs.
- ✅ El chatbot recibe una pregunta, la vectoriza, busca los embeddings similares en la colección de Qdrant, y utiliza el contexto encontrado para generar una respuesta coherente y precisa.
- ✅ Clasificación de textos utilizando **KMeans** y **Multinomial Naive Bayes**, con visualización de las predicciones.
- ✅ Visualización interactiva con **Pandas** y **Streamlit**, mostrando el texto procesado y su vectorización.

---

📌 **Tecnologías utilizadas**

- `pdfplumber` **→** Para extraer texto y tablas de PDFs estructurados.
- `pdfminer.six` **→** Para extraer contenido de PDFs con solo texto.
- `pytesseract + Tesseract OCR` **→** Para reconocer texto en imágenes dentro de PDFs escaneados.
- `NLTK` **→** Para normalizar el texto (eliminar stopwords, lematizar, etc.).
- `Word2Vec` **→** Para vectorizar el texto utilizando un enfoque basado en redes neuronales, mejorando la calidad de los embeddings.
- `Qdrant` **→** Base de datos vectorial utilizada para almacenar y recuperar los embeddings generados.
- `TinyLlama/TinyLlama-1.1B-Chat-v1.0` **→** Modelo de IA generativo utilizado para responder preguntas sobre el contenido del PDF.
- `Pandas` **→** Para estructurar y visualizar los datos en formato tabular.
- `KMeans` **→** Para agrupar y clasificar textos mediante clustering.
- `Multinomial Naive Bayes` **→** Para la clasificación de textos basada en probabilidades.
- `Streamlit` **→** Para una interfaz web interactiva.

---


📌 **Arquitectura y Orquestación**

- **Docker**: Se han agregado los archivos necesarios para empaquetar el proyecto en un contenedor Docker, facilitando la implementación y escalabilidad del proyecto en diferentes entornos.
- **Kubernetes**: Se ha configurado la orquestación de contenedores con Kubernetes, permitiendo gestionar, desplegar y escalar el proyecto de manera más eficiente en entornos distribuidos.

---

### Pre-requisitos ⚙️
Para poder usar este programa correctamente necesita:

- Python
- Tesseract OCR
- Poppler
- Docker (opcional)
- Kubernetes (opcional)
- minikube (opcional)

## 📌 Para utilizar este programa siga los siguientes pasos:

1. **Instalar las dependencias necesarias:** 
````bash
pip install -r requirements.txt
````

2. **Ejecutar la interfaz:**
````bash
streamlit run app.py
````

3. **Acceder al programa:**

`http://localhost:8501`

## 📌 Empaquetar el proyecto en un contenedor Docker:
1. Construir la imagen Docker:
````bash
docker build -t pdf-processing-app .
````
2. Subir contenedor a Docker hub:
````bash
docker login
docker tag mi-api-pdf  <UserName>/pdf-processing-app 
docker push <UserName>/pdf-processing-app 
````

## 📌 Orquestar el proyecto en Kubernetes:
````bash
minikube start 
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
````