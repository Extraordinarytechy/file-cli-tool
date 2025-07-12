import argparse


def count_lines(filename):
    """Return the number of lines in the file."""
    with open(filename, 'r') as f:
        return len(f.readlines())


def word_frequency(filename):
    """Return a dictionary of word frequencies in the file."""
    with open(filename, 'r') as f:
        words = f.read().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def main():
    parser = argparse.ArgumentParser(description='File CLI Tool')
    parser.add_argument('command', choices=['count-lines', 'word-frequency'])
    parser.add_argument('filename')

    args = parser.parse_args()

    if args.command == 'count-lines':
        print(count_lines(args.filename))
    elif args.command == 'word-frequency':
        print(word_frequency(args.filename))


if __name__ == '__main__':
    main()
