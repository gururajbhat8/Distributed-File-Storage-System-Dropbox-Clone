import os
from app.data_structures.content_hash import generate_sha256_hash
from app.core.config import STORAGE_DIR
from app.data_structures.bloom_filter import BloomFilter
from pathlib import Path


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
        
        # Initialize and populate the filter on every startup (first instantiation)
        self.bloom_filter = BloomFilter(num_items=1_000_000, false_positive_prob=0.01)
        self._populate_bloom_filter()
        self._initialized = True

    def _populate_bloom_filter(self) -> None:
        # Use STORAGE_DIR directly as it's already a Path object
        for path in STORAGE_DIR.iterdir():
            if path.is_file():
                # The filename is the hash
                self.bloom_filter.add(path.name)

    def save(self, data: bytes) -> str:
        file_hash = generate_sha256_hash(data)
        file_path = STORAGE_DIR / file_hash
        
        # Check Bloom Filter first for potential duplicates
        if file_hash in self.bloom_filter:
            # Perform expensive disk check to confirm
            if file_path.exists():
                # Real duplicate found, return hash without writing
                return file_hash
        
        # Hash not in filter or false positive - write to disk
        with open(file_path, 'wb') as f:
            f.write(data)
        
        # Add the hash to the filter after successful write
        self.bloom_filter.add(file_hash)
        
        return file_hash

    def load(self, file_hash: str) -> bytes | None:
        # Use pathlib for consistent path handling
        file_path = STORAGE_DIR / file_hash

        if not file_path.exists():
            # BUG FIX: Return None if the file doesn't exist, not the path.
            return None

        with open(file_path, 'rb') as f:
            return f.read()
