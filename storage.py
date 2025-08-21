import json

FILENAME = "tasks.json"

def load_tasks():
    """Load tasks from the file, or return an empty list if file not found."""
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks into the file."""
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)
