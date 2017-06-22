#!/usr/bin/python3

"""
Read a given string.
Change the character at a given index and then print the modified string.
"""

if __name__ == '__main__':
    N, M = map(int, input().split())
    PATTERN = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
    print('\n'.join(PATTERN + ['WELCOME'.center(M, '-')] + PATTERN[::-1]))
