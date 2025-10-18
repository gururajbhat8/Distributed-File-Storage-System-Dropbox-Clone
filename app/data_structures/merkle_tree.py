from typing import List, Optional
from app.data_structures.content_hash import generate_sha256_hash

class Node:
    def __init__(self, hash_value:str, left:Optional['Node'] = None, right:Optional['Node']= None):
        self.hash_value = hash_value
        self.left = left
        self.right = right


class MarkleTree:
    def __init__(self, chunk_hashes:List[str]):
        self.chunk_hashes = chunk_hashes
        self.root: Optional[Node] = None
        self.root = self._build_tree()

    def _build_tree(self) -> Optional[Node]:
        current_level = [Node(hash_value=chunk_hash) for chunk_hash in self.chunk_hashes]
        
        if not current_level:
            return None
        
        while len(current_level) > 1:
            next_level = []

            #to be continued