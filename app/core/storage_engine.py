import os
from app.data_structures.content_hash import generate_sha256_hash
from app.core.config import STORAGE_DIR


class StorageEngine:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # This check ensures the init logic runs only once.
        if hasattr(self, '_initialized'):
            return
        if not STORAGE_DIR.exists():
            os.makedirs(STORAGE_DIR)
        self._initialized = True

    def save(self, data: bytes) -> str:
        file_hash = generate_sha256_hash(data)
        # Use pathlib for consistent path handling
        file_path = STORAGE_DIR / file_hash

        with open(file_path, 'wb') as f:
            f.write(data)

        return file_hash

    def load(self, file_hash: str) -> bytes | None:
        # Use pathlib for consistent path handling
        file_path = STORAGE_DIR / file_hash

        if not file_path.exists():
            # BUG FIX: Return None if the file doesn't exist, not the path.
            return None

        with open(file_path, 'rb') as f:
            return f.read()
