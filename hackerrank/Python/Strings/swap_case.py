#!/usr/bin/python3

"""
SWAP CASE
"""


def swap_case(string):
    """ SWAP CASE """
    res = ""
    for i in range(0, len(string)):
        if string[i].islower():
            res += string[i].upper()
        elif string[i].isupper():
            res += string[i].lower()
        else:
            res += string[i]

    return res

# basically, we could just return "string.swapcase()"


if __name__ == '__main__':
    S = input()
    RESULT = swap_case(S)
    print(RESULT)
