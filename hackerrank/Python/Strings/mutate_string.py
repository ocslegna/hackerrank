#!/usr/bin/python3

"""
Read a given string, change the character at a given index
and then print the modified string.
"""


def mutate_string(string, position, character):
    """ mutate string. """
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    STR = input()
    I, C = input().split()
    NEW_STR = mutate_string(STR, int(I), C)
    print(NEW_STR)
