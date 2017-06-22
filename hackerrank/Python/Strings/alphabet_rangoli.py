#!/usr/bin/python3

"""
Capitalize each word of a string
"""


def capitalize(string):
    """ Capitalize each word of a string """
    return ' '.join(c.capitalize() for c in string.split(' '))


if __name__ == '__main__':
    STRING = input()
    print(capitalize(STRING))
