#!/usr/bin/python3

"""
Split and join.
"""


def split_and_join(line):
    """ Split and join. """
    return "-".join(line.split(" "))


if __name__ == '__main__':
    LINE = input()
    RESULT = split_and_join(LINE)
    print(RESULT)
