from src.reader import read_csv
from src.document_builder import build_document
from src.embedder import generate_embedding
from src.writer import save_embedding
from src.checkpoint import load_checkpoint, save_checkpoint

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

    first_row = chunk.iloc[0]

    document = build_document(first_row)

    embedding = generate_embedding(document)

    print(f"Embedding Dimension: {len(embedding)}")

    save_embedding(first_row, embedding)

    print("Saved Successfully")

    # IMPORTANT
    save_checkpoint(index)

    print(f"Checkpoint Saved: {index}")

    break