#!/usr/bin/python3

"""
Execute N commands given in N lines.
"""


if __name__ == '__main__':
    N = int(input())
    S = set(map(int, input().split()))
    for i in range(int(input())):
        eval('S.{0}({1})'.format(*input().split() + ['']))

    print(sum(S))
