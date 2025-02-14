import streamlit as st 
import os
from src.texto import texto 
from src.texto_y_tablas import texto_y_tablas
from src.texto_de_img import texto_de_img

st.title("📄 Procesador de PDF")

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
        
    #Eliminar PDF temporal
    os.remove(pdf_path)