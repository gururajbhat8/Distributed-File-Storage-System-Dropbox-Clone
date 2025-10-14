# 🎯 Distributed File Storage System (Dropbox Clone)

This project is a production-grade distributed file storage system built from scratch. It serves as a practical learning ground for mastering advanced Data Structures & Algorithms (DSA), Object-Oriented Programming (OOP) design patterns, and systems design principles.

---

## 🌟 Core Features (Current & Planned)

-   **Content-Addressable Storage:** Files are stored and retrieved based on the hash of their content, not their name.
-   **Smart Deduplication:** Save significant storage space by never storing the same piece of data twice.
-   **Advanced Chunking:**
    -   `FixedSizeChunking`: Simple and fast.
    -   `ContentDefinedChunking`: Robust against small file modifications, maximizing deduplication.
-   **File Versioning (Planned):** Keep a complete history of file changes and allow rollbacks.
-   **Large File Support (Planned):** Efficiently handle large files through streaming and chunking.
-   **Real-time Sync (Planned):** Use WebSockets for multi-client synchronization with conflict resolution.

---

## 📚 Concepts & Technologies

This project is a deep dive into the following concepts:

### Core Data Structures:
-   **Hash Map:** For content-addressable storage and deduplication.
-   **Merkle Tree (Planned):** For file integrity verification and versioning.
-   **Trie (Planned):** For fast file path lookups.
-   **Bloom Filter (Planned):** For quick, space-efficient duplicate detection.

### Algorithms:
-   **SHA-256 Hashing:** For content addressing and identification.
-   **Rolling Hash (Rabin-Karp):** For efficient content-defined chunking.

### OOP Design Patterns:
-   **Singleton:** For the global `StorageEngine`.
-   **Strategy:** For swappable `ChunkingStrategy` algorithms.
-   **Factory:** For `FileObject` creation.
-   **Observer (Planned):** For file change notifications.
-   **Decorator (Planned):** For adding layers like compression or encryption.

---

## 🏗️ Project Structure

```
distributed-file-storage/
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── storage_engine.py
│   ├── data_structures/
│   │   └── content_hash.py
│   ├── models/
│   │   └── file.py
│   ├── services/
│   │   └── file_service.py
│   └── strategies/
│       └── chunking.py
├── storage/
├── tests/
├── requirements.txt
└── README.md
```