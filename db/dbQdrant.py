from qdrant_client import QdrantClient
from langchain.vectorstores import Qdrant
from qdrant_client.models import PointStruct

qdrant = QdrantClient(
    url="https://c0ecc735-4daa-4faf-8e47-87ec35ba28bc.europe-west3-0.gcp.cloud.qdrant.io:6333", 
    https=True,
    api_key="zXQmNpc6rGfyeSiibzntmDDph_xegr3cI1DoiK5hvK6Uj2WYGKcTdA",
)


def validar_collection(collection_name, embeddings):
    existing_collections = qdrant.get_collections()
    if collection_name in [col.name for col in existing_collections.collections]:
        print(f"La colección '{collection_name}' ya existe.")
    else:
        print(f"La colección '{collection_name}' no existe. Creándola...")
        qdrant.recreate_collection(
            collection_name=collection_name,
            vectors_config={"size": len(embeddings[0]), "distance": "Cosine"}
        )

def add_embeddings_to_bd(embeddings, metadatos =None, collection_name =""):
    validar_collection(collection_name, embeddings)
    if metadatos is None:
        metadatos= [{}] * len(embeddings)
        
    qdrant.upsert(
        collection_name = collection_name,
        points=[
            PointStruct(
                id = i,
                vector = vector,
                payload={"description": " ".join(metadatos[i])}            
                )
            for i, vector in enumerate(embeddings)
        ]
    )
    
    vector_store = Qdrant(
        client=qdrant,
        collection_name=collection_name,
        embeddings=embeddings
    )
    
    return (f"Se insertaron {len(embeddings)} embeddings en '{collection_name}'.")

def obtener_embeddings(collection_name):
    embeddings = []
    scroll_response = qdrant.scroll(collection_name=collection_name, limit=1000)

    while scroll_response and scroll_response[0]:
        for point in scroll_response[0]:
            embeddings.append({
                "id": point.id, 
                "texto": point.payload["description"]
            })

        # Continuamos con la siguiente página utilizando el scroll_token
        scroll_token = scroll_response[1]
        if not scroll_token:
            break

        # Continuamos el scroll utilizando el token de paginación
        scroll_response = qdrant.scroll(collection_name=collection_name, scroll_token=scroll_token)

    return embeddings

def busqueda_similares(query, collection_name, top=5):
    respuesta = qdrant.search(
        collection_name=collection_name,
        query_vector=query,
        limit=top
    )
    return respuesta
