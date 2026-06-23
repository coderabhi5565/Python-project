def build_document(row):
    document = f"""
Movie: {row['title']}
Year: {row['year']}
Genres: {row['genres']}
Rating: {row['average_rating']}
Votes: {row['num_votes']}
"""
    return document.strip()