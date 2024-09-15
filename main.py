import csv
import sys
from collections import Counter

OUTPUT_FILE = "keywords_output.csv"


def read_csv_to_counter(filename):
    token_count = Counter()
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                for token in row:
                    token = token.strip()
                    if token:
                        token_count[token] += 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    return token_count


def write_counter_to_csv(token_count):
    with open(OUTPUT_FILE, "w", newline="") as output_file:
        writer = csv.writer(output_file)
        for token, count in token_count.most_common():
            writer.writerow([token, count])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py input_file.csv")
        sys.exit(1)

    input_filename = sys.argv[1]

    token_count = read_csv_to_counter(input_filename)
    write_counter_to_csv(token_count)

    keywords_before = token_count.total()
    keywords_after = len(token_count)
    ratio = keywords_after / keywords_before * 100

    print(
        f"Output written to {OUTPUT_FILE}.\n"
        f"Number of keywords before {keywords_before:,}, {keywords_after:,}, {ratio:.2%}"
    )
