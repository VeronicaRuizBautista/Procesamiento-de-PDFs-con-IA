from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from db.dbQdrant import busqueda_similares
from src.vectorizar import vectorizar_parrafo

MODELO_HF = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(MODELO_HF)
modelo = AutoModelForCausalLM.from_pretrained(
    MODELO_HF,
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True,  # Optimiza RAM
    device_map="auto"  # Carga automática en GPU si está disponible
)

device = "cuda" if torch.cuda.is_available() else "cpu"

def generar_contexto(data):
    textos = [p.payload["description"] for p in data]
    contexto = "\n".join(textos)
    print(contexto)
    return contexto

def chatbot(query, collection_name):
    # Convertir la pregunta en embedding antes de buscar en Qdrant
    pregunta = vectorizar_parrafo(query)
    data = busqueda_similares(pregunta, collection_name)
    contexto = generar_contexto(data)

    prompt = f"Contexto:\n{contexto}\n\nPregunta: {query}\n\nRespuesta: "
    
    entrada = tokenizer(prompt, return_tensors="pt").to(device)
    salida = modelo.generate(**entrada, max_new_tokens=50)
    respuesta = tokenizer.decode(salida[0], skip_special_tokens=True)

    # Extraer solo la parte después de "Respuesta:"
    if "Respuesta:" in respuesta:
        respuesta = respuesta.split("Respuesta:")[-1].strip()

    return respuesta