#!/usr/bin/env python3
import os
import re
import random
import sys

def shuffle():
    files = []
    for f in os.listdir("."):
        match = re.match('^([0-9]+-)?(.*\.pdf)', f, re.IGNORECASE)
        if match:
            files.append((f, match.group(2)))

    random.shuffle(files)
    for i in range(len(files)):
        name = "{:02d}-{}".format(i+1, files[i][1])
        name = name.replace(" ", "")
        name = name.replace("(", "")
        name = name.replace(")", "")
        name = name.replace("'", "")
        os.rename(files[i][0], name)
    return

def extract_names():
    files = []
    for f in os.listdir("."):
        match = re.match('^(([0-9]+)-)?(([^_]+)_.*\.pdf)', f, re.IGNORECASE)
        if match:
            files.append((int(match.group(2)), match.group(4)))

    files = sorted(files, key=lambda x: x[0])
    for i in range(len(files)):
        print(files[i][1])
    return

def main(argv):
    shuffle()
    return

def cli():
    main(sys.argv)

if __name__ == "__main__":
    main(sys.argv)
