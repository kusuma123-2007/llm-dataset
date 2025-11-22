import json

def create_jsonl(data, output_file):
    """
    Converts a list of dictionaries into JSONL format.
    Each dictionary becomes one line in the output file.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        for entry in data:
            json_line = json.dumps(entry, ensure_ascii=False)
            f.write(json_line + "\n")

if __name__ == "__main__":
    # Example data structure
    data = [
        {
            "title": "Basics of Human Immunity",
            "domain": "health",
            "source": "WHO Public Health Resources",
            "content": "The immune system protects the body..."
        }
    ]

    create_jsonl(data, "health_dataset_100.jsonl")
    print("JSONL file created successfully!")
