#!/usr/bin/python3

"""
Print True if set A is a strict superset of all other N sets. Otherwise, print False.
"""


if __name__ == '__main__':
    A = set(input().split())
    OTHER_SETS = int(input())
    for n in range(OTHER_SETS):
        if not A.issuperset(set(input().split())):
            print(False)
            exit(0)

    print(True)
