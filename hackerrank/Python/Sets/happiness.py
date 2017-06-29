#!/usr/bin/python3

"""
Calculate your happiness with disjoints sets A and B.
"""


def happiness(n, m, array, a, b):
    """ Calculate happiness """
    result = 0
    for n in array:
        if n in a:
            result += 1
        if n in b:
            result -= 1

    print(result)

if __name__ == '__main__':
    NUMS = list(map(int, input().split()))
    N = NUMS[0]
    M = NUMS[1]
    ARRAY = list(map(int, input().split()))
    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))
    happiness(N, M, ARRAY, A, B)
