# Procesamiento de PDFs 📜

Este proyecto permite extraer información de archivos PDF, incluyendo texto y tablas, tanto de documentos digitales como de PDFs escaneados. Utiliza pdfplumber para procesar textos y tablas en PDFs estructurados, pdfminer.six para extraer la información de PDFs con solo texto y Tesseract OCR para reconocer texto en imágenes dentro de PDFs escaneados. Además, ofrece una interfaz interactiva con Streamlit, permitiendo a los usuarios cargar archivos y seleccionar entre distintas opciones de extracción.

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