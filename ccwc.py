import os
import argparse
import sys

#https://docs.python.org/3/library/argparse.html#core-functionality


def ccwc(f_name, c, l, w):

    all = True if ((c and l and w) or (not c and not l and not w)) else False
    c = c or all
    l = l or all
    w = w or all

    output = ""

    try:
        file = open(f_name)
        file_stats = os.stat(f_name)

    except OSError:
        print(f_name + " can't be opened")
        return

    output += str(file_stats.st_size) + " bytes" if c else ""

    if l or w:
        lines = [line for line in file]
        if l:
            output += (" " + str(len(lines)) + " lines") if c else str(len(lines)) + " lines"

    words = 0
    for line in lines:
        words += len(line.split())

    if w:
        output += " " + str(words) + " words" if (c or l) else str(words) + " words"

    print(output + " " + f_name)

#sys.argv is a list of the command line arguments
#sys.argv[0] is the name of the python file

parser = argparse.ArgumentParser(
                    prog='wc_tool',
                    description='My version of wc',
                    epilog='Text at the bottom of help')

# parser.add_argument("-v", "--value")
# action="store_true" for an optional flag that is present or absent (no value)
parser.add_argument("-c", "--bytes", action="store_true")
parser.add_argument("-l", "--lines", action="store_true")
parser.add_argument("-w", "--words", action="store_true")

parser.add_argument("filename", nargs="?")
#nargs="?" makes the positional arg optional

args = parser.parse_args()
#print(args.bytes, args.lines, args.words, args.filename)

if not args.filename:
    print("You must provide a filename")
else:
    ccwc(args.filename, args.bytes, args.lines, args.words)
