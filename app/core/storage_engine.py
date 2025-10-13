import os
from app.data_structures.content_hash import generate_sha256_hash
from app.core.config import STORAGE_DIR


class StorageEngine:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        
        return cls._instance
    
    def __init__(self):
        if not os.path.exists(STORAGE_DIR):
            os.makedirs(STORAGE_DIR)

    def save(self, data: bytes) -> str:
        file_hash = generate_sha256_hash(data)
        file_path = os.path.join(STORAGE_DIR, file_hash)

        with open(file_path, 'wb') as f:
            f.write(data)

        return file_hash
    
    def load(self, file_hash:str) -> bytes | None:
        file_path = os.path.join(STORAGE_DIR, file_hash)

        if not os.path.exists(file_path):
            return file_path
        
        with open(file_path, 'rb') as f:
            return f.read()



