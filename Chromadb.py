
import chromadb

client = chromadb.Client()
collection = client.create_collection(name="my_collection")

collection.add(
    documents=[
        "This document is about New York",
        "This document is about Delhi"
    ],
    ids = ['id1', 'id2']
)
all_docs = collection.get()
all_docs

documents = collection.get(ids=["id1"])
documents
results = collection.query(
    query_texts=['Query is about big apple'],
    n_results=2
)
results

collection.delete(ids=all_docs['ids'])
collection.get()

collection.add(
    documents=[
        "This document is about New York",
        "This document is about Delhi"
    ],
    ids=["id3", "id4"],
    metadatas=[
        {"url": "https://en.wikipedia.org/wiki/New_York_City"},
        {"url": "https://en.wikipedia.org/wiki/New_Delhi"}
    ]
)

results = collection.query(
    query_texts=["Query is about Chhole Bhature"],
    n_results=2
)
results
