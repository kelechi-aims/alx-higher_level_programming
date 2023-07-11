#!/usr/bin/python3
'''This has a function that reads a text file (UTF8) and prints
   it to stdout.
'''


def read_file(filename=""):
    '''
    Reads a text and prints its content to stdout.#

    Args:
        filename (str): The name of the text file to read

    Returns:
        None
    '''
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
