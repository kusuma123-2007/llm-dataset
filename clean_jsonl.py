import json

def clean_jsonl(input_file, output_file):
    cleaned_entries = []
    unique_set = set()

    with open(input_file, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()

            if not line:
                continue  # skip empty lines

            try:
                entry = json.loads(line)

                # Convert entry to a hashable structure for duplicate removal
                entry_tuple = tuple(sorted(entry.items()))

                if entry_tuple not in unique_set:
                    unique_set.add(entry_tuple)
                    cleaned_entries.append(entry)

            except json.JSONDecodeError:
                print(f"Skipping invalid JSON line: {line}")

    # Write cleaned entries back to JSONL
    with open(output_file, "w", encoding="utf-8") as outfile:
        for entry in cleaned_entries:
            outfile.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"Cleaning complete: {len(cleaned_entries)} entries saved to {output_file}")


if __name__ == "__main__":
    clean_jsonl("health_dataset_100.jsonl", "health_dataset_clean.jsonl")
