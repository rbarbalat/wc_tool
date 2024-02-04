import os
import argparse
import sys


def ccwc(f_name):
    file = open(f_name)

    file_stats = os.stat(f_name)
    print(file_stats.st_size, " bytes")

    lines = [line for line in file]
    print(len(lines), " lines")

    words = 0
    for line in lines:
        words += len(line.split())

    print(words, " words")

filename = sys.argv[1]  #argv[0] is the name of the python script
ccwc(filename)
