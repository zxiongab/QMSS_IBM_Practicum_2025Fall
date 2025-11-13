#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 00:43:37 2025

@author: xinleicheng
"""

import json
import chromadb

with open("Physical_Data_Modelembedding (1).json", "r", encoding="utf-8") as f:
    data = json.load(f)

client = chromadb.PersistentClient(path="./chroma_physical_data_model")

collection = client.get_or_create_collection("physical_data_model")

ids = [f"section_{i}" for i in range(len(data))]
documents = [d["text"] for d in data]
embeddings = [d["embedding"] for d in data]

metadatas = [
    {
        "section_number": d.get("section_number", ""),
        "section_title": d.get("section_title", ""),
        "document": d.get("document", "Physical Data Model Template")
    }
    for d in data
]


collection.add(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)
