import json
import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    persist_directory="./Implementation_Phase_VectorDB"
))

# Create or get collection
collection = client.get_or_create_collection(name="implementation_phase_templates")

# List of embedding files
embedding_files = [
    "Business Analysis Impact_embedding.json",
    "CDC_UP_Lessons_Learned_Post_Project_Survey_embedding_output.json",
    "EPLC_Acquisition_Strategy_Template_embedding.json",
    "Lessons_Learned_Log_embedding.json",
    "SLA_MOU_embedding.json",
    "System_of_Records_Notice_embedding.json"
]

for file in embedding_files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    ids, texts, embeddings, metadatas = [], [], [], []

    for i, item in enumerate(data):
        if "embedding" not in item:
            continue  
        ids.append(f"{file}_{i}")
        texts.append(item.get("text", ""))
        embeddings.append(item["embedding"])
        metadatas.append({
            "file": file,
            "section_number": item.get("section_number", ""),
            "section_title": item.get("section_title", "")
        })

    if embeddings:
        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas
        )
    else:
        print(f"⚠️ Skipped {file} — no embeddings found.")

