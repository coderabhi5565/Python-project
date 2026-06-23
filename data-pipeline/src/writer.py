import os
import pandas as pd


OUTPUT_FILE = "output/embeddings.csv"


def save_embedding(row, embedding):
    data = {
        "imdb_id": row["imdb_id"],
        "title": row["title"],
        "year": row["year"],
        "genres": row["genres"],
        "average_rating": row["average_rating"],
        "num_votes": row["num_votes"],
        "embedding": str(embedding)
    }

    df = pd.DataFrame([data])

    file_exists = os.path.exists(OUTPUT_FILE)

    df.to_csv(
        OUTPUT_FILE,
        mode="a",
        header=not file_exists,
        index=False
    )