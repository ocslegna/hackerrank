#!/usr/bin/python3

"""
You are given a string S.
Your task is to print all possible size k replacement
 combinations of the string in lexicographic sorted order.
"""


from itertools import combinations_with_replacement


if __name__ == '__main__':
    STR, N = input().split()
    print('\n'.join([''.join(tuple) for tuple in combinations_with_replacement(''.join(sorted(STR)), int(N))]))
