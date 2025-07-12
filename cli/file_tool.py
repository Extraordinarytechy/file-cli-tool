import argparse
from collections import Counter
import os


def count_lines(filename):
    """Returns the number of lines in the file."""
    with open(filename, 'r') as file:
        return len(file.readlines())


def word_frequency(filename):
    """Returns a dict of word frequencies (lowercased)."""
    with open(filename, 'r') as file:
        words = file.read().lower().split()
        return dict(Counter(words))


def run_cli():
    parser = argparse.ArgumentParser(
        description="File CLI Tool — count lines or word frequency."
    )
    parser.add_argument("operation", choices=["count", "freq"], help="Choose operation")
    parser.add_argument("filename", help="Path to file")
    args = parser.parse_args()

    if not os.path.exists(args.filename):
        print("[Error] File not found.")
        return

    if args.operation == "count":
        print("Line Count:", count_lines(args.filename))
    elif args.operation == "freq":
        freqs = word_frequency(args.filename)
        for word, freq in freqs.items():
            print(f"{word}: {freq}")


if __name__ == "__main__":
    run_cli()

