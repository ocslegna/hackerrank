#!/usr/bin/python3

"""
Use wrap/fill
"""

import textwrap


def wrap(string, max_width):
    """ Use wrap/fill """
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    STR, MAX_WIDTH = input(), int(input())
    RES = wrap(STR, MAX_WIDTH)
    print(RES)
