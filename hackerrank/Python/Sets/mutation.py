#!/usr/bin/python3

"""
mutation set.
"""


if __name__ == '__main__':
    input()
    L = set(input().split())
    for _ in range(int(input())):
        command, *args = input().split()
        getattr(L, command)(set(input().split()))
    print(sum(map(int, L)))
