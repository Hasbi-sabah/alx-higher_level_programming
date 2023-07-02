#!/usr/bin/python3
def text_indentation(text):
    """
    A function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text : Argument

    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    delims = ['.', '?', ':']
    new_text = []
    line = ""
    for letter in text:
        line += letter
        if letter in delims:
            new_text.append(line.strip())
            line = ""
    new_text.append(line.strip())
    for line in new_text:
        print(line, end='\n\n')
