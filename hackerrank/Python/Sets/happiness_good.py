#!/usr/bin/python3

"""
Calculate your happiness with disjoints sets A and B.
"""


if __name__ == '__main__':
    NUMS = list(map(int, input().split()))
    N = NUMS[0]
    M = NUMS[1]
    ARRAY = list(map(int, input().split()))
    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))
    print(sum([(i in A) - (i in B) for i in ARRAY]))
