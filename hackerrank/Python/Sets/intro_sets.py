#!/usr/bin/python3

"""
Output the average height value on a single line.
"""


if __name__ == '__main__':
    N = int(input())
    ARR = list(map(int, input().split()))
    RESULT = sum(set(ARR))/len(set(ARR))
    print(RESULT)
