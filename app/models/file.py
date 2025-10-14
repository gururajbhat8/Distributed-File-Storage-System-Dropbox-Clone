from pydantic import BaseModel, Field
from typing import List

class Chunk(BaseModel):
    chunk_hash : str
    data : bytes
    chunk_order : int

class FileObject(BaseModel):
    filename: str
    size:int
    chunk_hashes: List[str] = Field(default_factory=list)