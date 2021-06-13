#!/usr/bin/env python
"""We have a directory with files that have same extension, in our case `.txt`.
Reading all files from a directory to find the longest word from each files.
"""

import os

path = "./"
os.chdir(path)


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        words = f.read().split()
        max_words = max(words, key=len)
        max_len = len(max(words, key=len))
        print("The longest word is %s in length of %d characters" % (max_words, max_len))


def main():
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{path}\{file}"
            read_text_file(file_path)


if __name__ == "__main__":
    main()
