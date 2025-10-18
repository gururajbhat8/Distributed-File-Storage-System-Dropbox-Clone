from app.core.storage_engine import StorageEngine
from app.models.file import FileObject
from app.strategies.chunking import ChunkingStrategy, FixedSizeChunking


class FileFactory:
    def __init__(self):
        self.storage_engine = StorageEngine()

    def create_file_object(self, filename: str, file_data: bytes, strategy: ChunkingStrategy = FixedSizeChunking()) -> FileObject:
        
        chunk_hashes = []

        for chunk in strategy.execute(file_data):
            chunk_hash = self.storage_engine.save(chunk)
            chunk_hashes.append(chunk_hash)

        # The FileObject should be created and returned only after the loop is complete.
        return FileObject(
            filename=filename,
            size=len(file_data),
            chunk_hashes=chunk_hashes
        )