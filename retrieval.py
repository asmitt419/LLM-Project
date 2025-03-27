import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

function_map = {
    "open_chrome": "Launch Google Chrome browser",
    "open_calculator": "Open the calculator application",
    "get_cpu_usage": "Retrieve the current CPU usage",
    "get_ram_usage": "Retrieve the current RAM usage",
}

descriptions = list(function_map.values())
embeddings = model.encode(descriptions)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def retrieve_function(user_query):
    query_embedding = model.encode([user_query])
    _, idx = index.search(query_embedding, 1)
    return list(function_map.keys())[idx[0][0]]
