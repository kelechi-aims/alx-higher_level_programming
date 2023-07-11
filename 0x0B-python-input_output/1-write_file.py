#!/usr/bin/python3
'''Has a function that writes a string to a text file and returns
   the number of characters written:
'''


def write_file(filename="", text=""):
    '''
    Writes a string to a text file.

    Args:
        filename (str): The name of the text file.
                        Default to empty string
        text (str): Text to be written to the file.
                    default to empty string.

        Returns: The number of characters written.
    '''
    with open(filename, mode='w', encoding='utf-8') as file:
        nb_characters = file.write(text)
        return nb_characters
