import os
import argparse
import sys

#https://docs.python.org/3/library/argparse.html#core-functionality

#https://codingchallenges.fyi/challenges/challenge-wc
def ccwc(f_name, c, l, w, pipe):

    all = True if ((c and l and w) or (not c and not l and not w)) else False
    c = c or all
    l = l or all
    w = w or all

    output = ""

    if f_name:
        try:
            file = open(f_name)
            file_stats = os.stat(f_name)
            num_bytes = file_stats.st_size

        except OSError:
            print(f_name + " can't be opened")
            return

    #read from std input IF filename NOT provided
    elif pipe:
        file = sys.stdin

    if c and not pipe:
        output += str(num_bytes)

    if l or w or (c and pipe):
        lines = [line for line in file]

        if c and pipe:
            num_bytes = sum([len(line.encode("utf8")) for line in lines])
            output += str(num_bytes)

        if l:
            output += (" " + str(len(lines))) if c else str(len(lines))

    if w:
        words = 0
        for line in lines:
            words += len(line.split())

        output += " " + str(words) if (c or l) else str(words)

    output += " " + f_name if f_name else ""
    print(output)

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

pipe = not sys.stdin.isatty()
#sys.stdin.isatty() is True if something was piped in

if not args.filename and not pipe:
    print("You must provide a filename on the command line or pipe a file")
elif args.filename and pipe:
    print("You must provide a filename or pipe a file but NOT BOTH")
else:
    ccwc(args.filename, args.bytes, args.lines, args.words, pipe)
