#!/usr/bin/env python
"""We have a directory with files that have same extension, in our case `.txt`.
First approach is to read from one file.
"""


def longest_word(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
        max_words = max(words, key=len)
        max_len = len(max(words, key=len))
        print("The longest word is %s in length of %d characters" % (max_words, max_len))


def main():
    longest_word('file1.txt')


if __name__== "__main__":
    main()