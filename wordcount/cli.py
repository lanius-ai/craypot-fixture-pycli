"""Command-line word frequency counter.

Usage: python -m wordcount [--top N] FILE [FILE ...]

Prints one line per word, "<count> <word>", most frequent first.
"""

import argparse
import sys
from collections import Counter


def count_words(text):
    counts = Counter()
    for word in text.split(" "):
        word = word.strip()
        if word:
            counts[word] += 1
    return counts


def rank(counts, top=None):
    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    if top is not None:
        ranked = ranked[:top]
    return ranked


def main(argv=None):
    parser = argparse.ArgumentParser(prog="wordcount", description="Count word frequencies.")
    parser.add_argument("--top", type=int, default=None, help="only print the N most frequent words")
    parser.add_argument("files", nargs="+", help="text files to read ('-' for stdin)")
    args = parser.parse_args(argv)
    if args.top is not None and args.top < 1:
        parser.error("--top must be at least 1")

    counts = Counter()
    for name in args.files:
        if name == "-":
            text = sys.stdin.read()
        else:
            with open(name, encoding="utf-8") as f:
                text = f.read()
        counts.update(count_words(text))

    for word, n in rank(counts, args.top):
        print(f"{n} {word}")
    return 0
