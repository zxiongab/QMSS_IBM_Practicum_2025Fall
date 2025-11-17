import json
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer


json_files = [
    "Training Plan.json",
    "Test Case.json",
    "SLA_MOU.json",
    "Operation.json"
]

rows = []


for file in json_files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    for section in data["sections"]:
        rows.append({
            "document": data["document_title"],
            "section_number": section["number"],
            "title": section["title"],
            "content": section.get("content") or ""
        })
        for sub in section.get("subsections", []):
            rows.append({
                "document": data["document_title"],
                "section_number": sub["number"],
                "title": sub["title"],
                "content": sub.get("content") or ""
            })

df = pd.DataFrame(rows)

model = SentenceTransformer("BAAI/bge-large-en-v1.5")
df["embedding"] = df["content"].apply(lambda x: model.encode(x).tolist())


chroma_client = chromadb.PersistentClient(path="./Development_Phase_VectorDB")
collection = chroma_client.get_or_create_collection("development_phase_templates")

ids = [f"{row['document']}_{row['section_number']}_{i}" for i, row in df.iterrows()]

collection.add(
    ids=ids,
    documents=df["content"].tolist(),
    embeddings=df["embedding"].tolist(),
    metadatas=[
        {"document": row["document"], "section_number": row["section_number"], "title": row["title"]}
        for _, row in df.iterrows()
    ]
)