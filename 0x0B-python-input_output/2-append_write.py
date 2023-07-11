#!/usr/bin/pythons
'''Has a function that appends a string at the end of the text file
   (UTF8) and returns the number of characters added.
'''


def append_write(filename="", text=""):
    '''
    Appends string at the end of a text file.

    Args:
        filename (str): The name of the text file to append the text to.
                        Default to an empty string.
        text (str): The text to append the the file. Default to
                    empty string.

    Returns:
        The number of characters appended.
    '''
    with open(filename, mode='a', encoding='utf-8') as file:
        nb_characters = file.write(text)
        return nb_characters
