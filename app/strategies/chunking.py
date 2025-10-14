from abc import ABC, abstractmethod
from typing import Iterator


class ChunkingStrategy(ABC):

    @abstractmethod
    def execute(self, data: bytes) -> Iterator[bytes]:
        pass


class FixedSizeChunking(ChunkingStrategy):
    """Implements chunking based on a fixed size."""

    CHUNK_SIZE = 4 * 1024 * 1024  # 4MB

    def execute(self, data: bytes) -> Iterator[bytes]:
        for i in range(0, len(data), self.CHUNK_SIZE):
            yield data[i : i + self.CHUNK_SIZE]

class ContentDefinedChunkiong(ChunkingStrategy):
    WINDOW_SIZE = 64
    TARGET_AVG_SIZE = 1*1024*1024
    CUT_POINT_MASK = TARGET_AVG_SIZE - 1
    MIN_CHUNK_SIZE = TARGET_AVG_SIZE // 4
    MAX_CHUNK_SIZE = TARGET_AVG_SIZE * 4

    def execute(self, data:bytes) -> Iterator[bytes]:
        if len(data) == 0 :
            return 
        
        start_of_chunk = 0

        for i in range(self.MIN_CHUNK_SIZE, len(data)):
            current_chunk_size = i - start_of_chunk

            if current_chunk_size > self.MAX_CHUNK_SIZE:
                yield data[start_of_chunk:i]
                start_of_chunk = i
                continue
        
