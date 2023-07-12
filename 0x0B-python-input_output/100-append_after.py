#!/usr/bin/python3
'''Has function that inserts a line of text to a file, after each line
   containing a specific string
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Inserts a line of text after each line conataining a specific
    string in a file

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each.
        new_string (str): The line of text to insert after each matching
                          line.
    '''
    lines = []
    with open(filename, mode='r') as file:
        for line in file:
            lines.append(line.rstrip())
            if search_string in line:
                lines.append(new_string)

    with open(filename, mode='w') as file:
        file.write("".join(lines))
