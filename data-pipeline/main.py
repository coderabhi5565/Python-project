from src.reader import read_csv
from src.document_builder import build_document
from src.embedder import generate_embedding
from src.writer import save_embedding
from src.checkpoint import load_checkpoint, save_checkpoint
from src.retry import retry

FILE_PATH = "data/imdb_top_movies_1980_2026.csv"

chunks = read_csv(FILE_PATH)

last_processed_chunk = load_checkpoint()

print(f"Last Processed Chunk: {last_processed_chunk}")

for index, chunk in enumerate(chunks, start=1):

    if index <= last_processed_chunk:
        print(f"Skipping Chunk {index}")
        continue

    print(f"\nProcessing Chunk {index}")
    print(f"Shape: {chunk.shape}")
    print("-" * 30)

    for row_number, (_, row) in enumerate(chunk.iterrows(), start=1):
        if row_number > 5:
            break
        
        print(f"\nProcessing Movie {row_number}")

        document = build_document(row)

        embedding = retry(
    lambda: generate_embedding(document)
)
        print(f"Embedding Dimension: {len(embedding)}")
        save_embedding(row, embedding)
        print("Saved Successfully")
    save_checkpoint(index)

    print(f"Checkpoint Saved: {index}")

    break