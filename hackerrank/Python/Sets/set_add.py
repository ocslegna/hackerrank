#!/usr/bin/python3

"""
Given country stamps, print the number of distinct country stamps.
"""


if __name__ == '__main__':
    N = int(input())
    COUNTRY_STAMPS = set([input() for i in range(N)])
    RESULT = set()
    for c in COUNTRY_STAMPS:
        if c not in RESULT:
            RESULT.add(c)

    print(len(RESULT))
