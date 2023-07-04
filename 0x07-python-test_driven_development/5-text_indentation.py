#!/usr/bin/python3
"""
Module to seperate text based on delims
"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text : Argument

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    delims = [".", "?", ":"]
    new_text = []
    line = ""
    for letter in text:
        line += letter
        if letter in delims:
            new_text.append(line.replace(" \n", "\n").replace("\n ", "\n"))
            line = ""
    else:
        if line != "":
            new_text.append(line.replace(" \n", "\n").replace("\n ", "\n"))
    for line in new_text:
        print(line.strip(" \t"), end="")
        for el in delims:
            if el in line:
                print(end="\n\n")
                break
