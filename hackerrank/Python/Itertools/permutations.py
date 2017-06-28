#!/usr/bin/python3

"""
You are given a string S.
Input: A single line containing the space separated string S and the integer value k.
Output: Print the permutations of the string S on separate lines.

Print all possible permutations of size k of the string in lexicographic sorted order.

If r is not specified or is None, then r defaults to the length of the iterable,
  and all possible full-length permutations are generated.
Permutations are emitted in lexicographic sort order.
So, if the input iterable is sorted, the permutation tuples will be produced in sorted order.
Elements are treated as unique based on their position, not on their value.
So if the input elements are unique, there will be no repeat values in each permutation.
"""


from itertools import permutations


if __name__ == '__main__':
    STR = input().split()
    print('\n'.join([''.join(tuple) for tuple in permutations(sorted(STR[0]), int(STR[1]))]))
