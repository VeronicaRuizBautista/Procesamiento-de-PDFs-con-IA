# Procesamiento, normalización y vectorización de PDFs 📜

Este proyecto permite extraer, normalizar y vectorizar información de archivos PDF, incluyendo texto y tablas, tanto de documentos digitales como de PDFs escaneados. Además, ofrece una interfaz interactiva con Streamlit, permitiendo a los usuarios cargar archivos y seleccionar entre distintas opciones de extracción y clasificación de texto.

🔹 **Características principales**

- ✅ Extracción de texto y tablas de PDFs digitales y escaneados.
- ✅ Normalización del texto con **NLTK**: eliminación de signos de puntuación, stopwords y lematización.
- ✅ Vectorización del texto usando **Scikit-Learn** para convertir el contenido en una representación numérica.
- ✅ Clasificación de textos utilizando **KMeans** y **Multinomial Naive Bayes**, con visualización de las predicciones.
- ✅ Visualización interactiva con **Pandas** y **Streamlit**, mostrando el texto procesado y su vectorización.

---

📌 **Tecnologías utilizadas**

- `pdfplumber` **→** Para extraer texto y tablas de PDFs estructurados.
- `pdfminer.six` **→** Para extraer contenido de PDFs con solo texto.
- `pytesseract + Tesseract OCR` **→** Para reconocer texto en imágenes dentro de PDFs escaneados.
- `NLTK` **→** Para normalizar el texto (eliminar stopwords, lematizar, etc.).
- `Scikit-Learn` **→** Para vectorizar el texto usando **CountVectorizer** o **TfidfVectorizer**.
- `Pandas` **→** Para estructurar y visualizar los datos en formato tabular.
- `KMeans` **→** Para agrupar y clasificar textos mediante clustering.
- `Multinomial Naive Bayes` **→** Para la clasificación de textos basada en probabilidades.
- `Streamlit` **→** Para una interfaz web interactiva.


### Pre-requisitos ⚙️
Para poder usar este programa correctamente necesita:

- Python
- Tesseract OCR
- Poppler

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