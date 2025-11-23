import json
import pandas as pd
import chromadb


chroma_client = chromadb.PersistentClient(path="./Implementation_Phase_VectorDB")
collection = chroma_client.get_or_create_collection("implementation_phase_templates")


embedding_files = [
    "Business Analysis Impact_embedding.json",
    "CDC_UP_Lessons_Learned_Post_Project_Survey_embedding_output.json",
    "EPLC_Acquisition_Strategy_Template_embedding.json",
    "Lessons_Learned_Log_embedding.json",
    "SLA_MOU_embedding.json",
    "System_of_Records_Notice_embedding.json"
]

rows = []


for file in embedding_files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    for item in data:
        text = item.get("text") or item.get("content") or ""
        embedding = item.get("embedding")
        if not embedding or not isinstance(embedding, list):
            continue

        rows.append({
            "document": file,
            "section_number": item.get("section_number", item.get("number", "")),
            "section_title": item.get("section_title", item.get("title", "")),
            "text": text,
            "embedding": embedding
        })

df = pd.DataFrame(rows)

ids = [f"{row['document']}_{row['section_number']}_{i}" for i, row in df.iterrows()]

collection.add(
    ids=ids,
    documents=df["text"].tolist(),
    embeddings=df["embedding"].tolist(),
    metadatas=[
        {
            "document": row["document"],
            "section_number": row["section_number"],
            "section_title": row["section_title"]
        }
        for _, row in df.iterrows()
    ]
)

