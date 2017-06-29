#!/usr/bin/python3


"""
Just some probability
"""

from itertools import combinations


if __name__ == '__main__':
    N = int(input())
    L = input().split()
    K = int(input())

    C = list(combinations(L, K))
    F = filter(lambda c: 'a' in c, C)
    print("{0:.3}".format(len(list(F))/len(C)))
