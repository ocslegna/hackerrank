#!/usr/bin/python3

"""
Output the average height value on a single line.
"""


def average(array):
    return sum(set(array))/len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
