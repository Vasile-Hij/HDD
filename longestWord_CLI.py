#!/usr/bin/env python
"""We have a directory with files that have same extension, in our case `.txt`.
Second approach is to read from one file from command line.
"""
import argparse


def longest_word(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
        max_len = len(max(words, key=len))
        return [word for word in words if len(word) == max_len]


def main():
    parser = argparse.ArgumentParser(description="Read longest word")
    parser.add_argument('--file', required=True)
    args = parser.parse_args()

    read = longest_word(args.file)
    print(read)


if __name__ == "__main__":
    main()