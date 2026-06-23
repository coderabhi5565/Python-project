import json
import os

CHECKPOINT_FILE = "checkpoints/checkpoint.json"

def save_checkpoint(chunk_number):
    data = {
        "last_processed_chunk": chunk_number
    }

    os.makedirs("checkpoints", exist_ok=True)

    with open(CHECKPOINT_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_checkpoint():
    if not os.path.exists(CHECKPOINT_FILE):
        return 0

    with open(CHECKPOINT_FILE, "r") as file:
        data = json.load(file)

    return data.get("last_processed_chunk", 0)