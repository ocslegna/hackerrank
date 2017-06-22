#!/usr/bin/python3

"""
Given 2 int sets M and N, print their symmetric difference in asc order.
"""


def symmetric_difference(k, m, j, n):
    mdn = m.difference(n)
    ndm = n.difference(m)
    c = mdn.union(ndm)
    for n in sorted(c):
        print(n)


if __name__ == '__main__':
    k, M, j, N = input(), set(list(map(int, input().split()))), input(), set(list(map(int, input().split())))
    symmetric_difference(k, M, j, N)
