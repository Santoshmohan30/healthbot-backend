import chromadb
from chromadb.config import Settings

CHROMA_DIR = "data/chroma"
COLLECTION_NAME = "healthbot_kb"

def get_collection():
    client = chromadb.PersistentClient(
        path=CHROMA_DIR,
        settings=Settings(anonymized_telemetry=False),
    )
    return client.get_or_create_collection(name=COLLECTION_NAME)
