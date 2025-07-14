import csv
import os

def write_csv(data, path):
    """
    Writes a list of dictionaries to a CSV file.
    Creates the output folder if it doesn't exist.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
