#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print("{} argument{}:".format(num_arguments,
        's' if num_arguments != 1 else ''))
    for i, arg in enumerate(arguments, start=1):
        print("{}: {}".format(i, arg))
