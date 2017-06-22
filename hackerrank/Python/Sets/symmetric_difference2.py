#!/usr/bin/python3

"""
symmetric difference set.
"""


if __name__ == '__main__':
    N = int(input())
    E = set(map(int, input().split()))
    M = int(input())
    F = set(map(int, input().split()))
    print(len(E.symmetric_difference(F)))
