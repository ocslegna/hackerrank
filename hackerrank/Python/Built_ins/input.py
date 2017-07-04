#!/usr/bin/python3

"""
input():
"""

if __name__ == '__main__':
    # input must contain 'X'
    X, K = map(int, input().split())
    print(K == eval(input()))
