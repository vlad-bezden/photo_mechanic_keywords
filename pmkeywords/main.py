from collections import Counter
import csv
from pathlib import Path
import sys

OUTPUT_FILE = Path("keywords_output.csv")


def read_csv_to_counter(filename: Path) -> Counter:
    try:
        return Counter(
            token.strip()
            for row in csv.reader(filename.open())
            for token in row
            if token.strip()
        )
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        raise


def write_counter_to_csv(token_count: Counter) -> None:
    with OUTPUT_FILE.open("w", newline="") as f:
        csv.writer(f).writerows(token_count.most_common())


def print_output(token_count: Counter) -> None:
    keywords_before = token_count.total()
    keywords_after = len(token_count)

    print(f"Output written to {OUTPUT_FILE}.")
    print(
        f"Number of keywords: before {keywords_before:,}, "
        f"after {keywords_after:,}, reduction {keywords_before/keywords_after:,.0f}"
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py input_file.csv")
        sys.exit(1)

    token_count = read_csv_to_counter(Path(sys.argv[1]))
    write_counter_to_csv(token_count)
    print_output(token_count)
