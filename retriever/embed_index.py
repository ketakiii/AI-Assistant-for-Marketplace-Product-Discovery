# Importing necessary libraries
import json
import os 
import argparse
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# load the listings from the simuated data
def load_listings(file_path):
    """
    Load the product listings from a JSON file.
    """
    with open(file_path, 'r') as f:
        listings = json.load(f)
    return listings

# build the corpus from the listings
def build_corpus(listings):
    """
    Build a corpus of product listings.
    """
    return [
        f"{item['title']} - {item['category']} {item['description']} ({item['condition']}, ${item['price']})"
        for item in listings
    ], [item['id'] for item in listings]

# embed the corpus 
def embed_corpus(texts, model_name='all-MiniLM-L6-v2'):
    """
    Embed the corpus using a pre-trained SentenceTransformer model.
    """
    model = SentenceTransformer(model_name)
    return model.encode(texts, show_progress_bar=True)

# save the FAISS index to a file
def save_faiss_index(embeddings, ids, output_dir='embeddings'):
    """
    save the FAISS index to a file.
    """
    os.makedirs(output_dir, exist_ok=True)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, os.path.join(output_dir, 'index.faiss'))
    with open(os.path.join(output_dir, 'id_map.json'), 'w') as f:
        json.dump(ids, f, indent=4)
        print(f"FAISS index and ID map saved to {output_dir}")


def main(input_file, output_dir):
    print("Loading data from {input_file}")
    listings = load_listings(input_file)

    print('Building text corpus ')


