import hashlib


def generate_sha256_hash(data: bytes) -> str:
    hash_object = hashlib.sha256()
    hash_object.update(data)

    return hash_object.hexdigest()
