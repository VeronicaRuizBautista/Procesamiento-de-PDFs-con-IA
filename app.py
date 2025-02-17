import streamlit as st 
import os
from procesamientoPDFs.texto import texto 
from procesamientoPDFs.texto_y_tablas import texto_y_tablas
from procesamientoPDFs.texto_de_img import texto_de_img
from src.normalizar import normalizar
from src.vectorizar import vectorizar
import pandas as pd
from src.clasificacion import clasificar

st.title("📄 Procesamiento de PDFs y Análisis de Texto")

opcion = st.radio("Selecciona una opción", [
    "Extraer texto de PDF",
    "Extraer texto y tablas de PDF",
    "Extraer texto de PDF escaneado"
])

#subir PDF
pdf = st.file_uploader("📂 Carga un archivo PDF", type=["pdf"])

carpeta = "pdfTemporal"

#Crear la carpeta si no existe
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

texto_del_pdf = ""

if pdf is not None:
    st.success("✅ Archivo cargado correctamente")
    
    #guardar PDF temporalmente
    pdf_path = os.path.join(carpeta, pdf.name)
    with open(pdf_path, "wb") as f: #Abre el archivo en modo escritura binaria
        f.write(pdf.getbuffer()) #obtiene los datos binarios del archivo subido y f.write guarda estos datos en el archivo en la carpeta pdfTemporal.
        
    if opcion == "Extraer texto de PDF":
        texto_del_pdf = texto(pdf_path)
        st.text_area("📜 Texto extraído:", texto_del_pdf, height=300)
        
    elif opcion == "Extraer texto y tablas de PDF":
        texto_del_pdf, tablas = texto_y_tablas(pdf_path)
        st.text_area("📜 Texto extraído:", texto_del_pdf, height=300)
        st.write("📊 Tablas extraídas:", tablas)
        
    elif opcion == "Extraer texto de PDF escaneado":
        texto_del_pdf = texto_de_img(pdf_path)
        st.text_area("📜 Texto extraído:", texto_del_pdf, height=300)
    
    if st.button("🔍 Normalizar y vectorizar texto"):
        texto_normalizado = normalizar(texto_del_pdf)
        texto_vectorizado, palabras = vectorizar(texto_normalizado)
        st.session_state.texto_vectorizado = texto_vectorizado
        st.session_state.textos = texto_normalizado
        # Crear un DataFrame con las palabras como columnas
        df = pd.DataFrame(texto_vectorizado, columns=palabras)
        st.markdown("✨ Texto vectorizado:")
        st.dataframe(df)
        st.text_area("🔤 Palabras clave:", ", ".join(palabras), height=150)

    if st.button ("Aplicar modelo de clasificación de texto"):
        if "texto_vectorizado" in st.session_state:
            precision = clasificar(st.session_state.texto_vectorizado, st.session_state.textos)
            st.text_area("Precisión:", precision, height=50)
        else:
            st.warning("⚠️ Primero debes normalizar y vectorizar el texto.")
    #Eliminar PDF temporal
    os.remove(pdf_path)