from elasticsearch import Elasticsearch
import pandas as pd
from embed import Embed
import time
import os

index_name = os.getenv("INDEX_NAME")
folder = f"{os.getenv("WORKDIR")}/data/"
documents_file = "az900_notes_with_vectors.pkl"
es_url = os.getenv("ELASTICSEARCH_URL")

def load_pickle():
    '''
    load pickle file
    '''
    return pd.read_pickle(f"{folder}{documents_file}").set_index("doc_id")

def infer_es_mapping(df, vec_dim):
    '''
    Accepts a pandas dataframe and vector embedding dimension and generates elasticsearch index mapping properties dynamically.
    Index is keyword type.
    Fields end with "_vec" are dense vector types, while others are text types.
    '''
    similarity = 'cosine'    
    es_mapping = {}

    if type(df.index) == pd.Index :
        es_mapping[df.index.name] = {'type': 'keyword'}

    for col in df.columns:
        if col.endswith("_vec"):
            es_mapping[col] = {'type': 'dense_vector', 'dims': vec_dim, 'index': True, 'similarity':similarity}
        else:
            es_mapping[col] = {'type': 'text'}
    return es_mapping

def create_es_index(es_client, es_mapping_properties):
    '''
    Create elasticsearch index
    '''
    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": es_mapping_properties
        }
    }

    es_client.indices.delete(index=index_name, ignore_unavailable=True)
    es_client.indices.create(index=index_name, body=index_settings)

def index_documents(es_client):
    '''
    Index documents into elasticsearch index
    '''
    documents = pd.read_pickle(f"{folder}{documents_file}").to_dict(orient="records")
    for doc in documents:
        es_client.index(index=index_name, document=doc)

if __name__ == "__main__":
    df = load_pickle()
    es_mapping = infer_es_mapping(df, Embed().get_vec_dim())
    es_client = None
    while es_client is None:
        try:
            es_client = Elasticsearch(es_url)
            # Check if the cluster is available
            if es_client.ping():
                # print("Connected to Elasticsearch!")
                create_es_index(es_client, es_mapping)
                index_documents(es_client)
            else:
                raise ConnectionError("Elasticsearch cluster is unavailable.")
        except ConnectionError as e:
            print(f"Connection to Elasticsearch failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)
    
    
    
