import json
import os
from config.settings import FILE_PATH


def read_data():
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    except Exception as e:
        print(f"Error readling file : {e}")
        return []


def write_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
