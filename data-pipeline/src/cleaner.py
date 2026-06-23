def inspect_chunk(chunk):
    print("\n===== CHUNK ANALYSIS =====")

    print(f"Rows: {len(chunk)}")
    print(f"Columns: {len(chunk.columns)}")

    print("\nMissing Values:")
    print(chunk.isnull().sum())

    print("\nDuplicate Rows:")
    print(chunk.duplicated().sum())

    print("=" * 40)