#!/usr/bin/python3
'''
   Contains a function that prints a text with 2 new lines
   after each of these characters: ., ? and :
'''


def text_indentation(text):
    '''
    Prints a text with 2 new lines after each of the characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = [".", "?", ":"]
    lines = []
    line = ""

    for char in text:
        line += char

        if char in punctuations:
            lines.append(line.strip())
            line = ""

    if line:
        lines.append(line.strip())

    print("\n\n".join(lines))
