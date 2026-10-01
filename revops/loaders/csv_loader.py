import csv


def load_csv(path: str) -> list[dict]:
    """Read a CSV file and return its rows as dicts, exactly as they appear on disk.

    Every value comes back as a string. No type conversion, no validation.
    """
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))
