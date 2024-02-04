import os
import argparse
import sys


def ccwc(f_name, flag):

    output = ""

    try:
        file = open(f_name)

    except OSError:
        print(f_name + " can't be opened")
        print("You must use the format ccwc.py filename OR ccww.py -flag filename")
        print("Valid flags are -l, -c and -w (no more than one)")
        return

    if flag == "-c" or not flag:
        file_stats = os.stat(f_name)
        output += str(file_stats.st_size)
        if flag == "-c":
            print(output + " " + f_name)
            return


    lines = [line for line in file]
    if flag == "-l":
        print(str(len(lines)) + " " + f_name)
        return
    output += " " + str(len(lines))

    words = 0
    for line in lines:
        words += len(line.split())

    if flag == "-w":
        print(str(words) + " " + f_name)
        return
    output += " " + str(words)

    print(output + " " + f_name)

#argv[0] is the name of the python script
#print(sys.argv)

flag = sys.argv[1] if len(sys.argv) > 2 else None

if (flag and flag not in ["-c", "-l", "-w"]) or len(sys.argv) > 3:
    print("The only acceptable flags are -c, -l and -w and you must provide at most one flag.")
else:
    filename = sys.argv[-1]
    ccwc(filename, flag)
