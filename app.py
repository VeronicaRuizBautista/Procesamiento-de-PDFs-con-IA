import streamlit as st 
import os
from procesamientoPDFs.texto import texto 
from procesamientoPDFs.texto_y_tablas import texto_y_tablas
from procesamientoPDFs.texto_de_img import texto_de_img
from src.normalizar import normalizar
from src.vectorizar import vectorizar, vectorizar_parrafo
import pandas as pd
from src.clasificacion import clasificar
from db.dbQdrant import add_embeddings_to_bd
from chat.chatbot import chatbot
import uuid

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
    
    texto_normalizado = normalizar(texto_del_pdf)
    texto_vectorizado, palabras, vector = vectorizar(texto_normalizado)
    parrafo_vectorizado = vectorizar_parrafo(texto_normalizado)
    st.session_state.parrafo_vectorizado = parrafo_vectorizado
    st.session_state.textos = texto_normalizado
    # Crear un DataFrame con las palabras como columnas
    df = pd.DataFrame(texto_vectorizado, index=palabras)
    precision, clasificacion = clasificar(st.session_state.parrafo_vectorizado, st.session_state.textos)
    qdrant = add_embeddings_to_bd(st.session_state.parrafo_vectorizado, st.session_state.textos, "InfoPDFs")
    
    if st.button("🔍 Normalizar y vectorizar texto"):
        st.success("✅ Texto normalizado y vectorizado")
        st.markdown("✨ Texto vectorizado:")
        st.dataframe(df)
        st.text_area("🔤 Palabras clave:", ", ".join(palabras), height=150)

    if st.button ("📇 Aplicar clasificación de texto"):
        if "parrafo_vectorizado" in st.session_state:    
            st.text_area("Resultados de clasificación:", "\n".join(clasificacion), height=300) 
            st.text_area("Precisión:", precision, height=100)
        else:
            st.warning("⚠️ Primero debes normalizar y vectorizar el texto.")
    
    if st.button("📥 Guardar data en bd"):
        if "parrafo_vectorizado" in st.session_state:
            st.text_area("✨ Data guardada en bd", qdrant, height=100)  
        else:
            st.warning("⚠️ Primero debes normalizar y vectorizar el texto.")
        
    st.title("🤖 Chatbot de PDFs 📄")
    if "thread_id" not in st.session_state:
        st.session_state.thread_id = str(uuid.uuid4())
        
    if "message_history" not in st.session_state:
        st.session_state.message_history = []
        
    for msg in st.session_state.message_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])   

    pregunta = ""
    pregunta = st.chat_input("Haz una pregunta sobre el pdf")
    if pregunta:
        st.session_state.message_history.append({"role": "user", "content": pregunta})
        with st.chat_message("user"):
            st.write(pregunta)
        
        with st.spinner("🧠 Pensando..."):
            repuesta = None
            respuesta = chatbot(pregunta, "InfoPDFs")
            
        with st.chat_message("bot"):
            st.write(respuesta)

    #Eliminar PDF temporal
    os.remove(pdf_path)