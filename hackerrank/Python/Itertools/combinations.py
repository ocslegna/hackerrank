#!/usr/bin/python3

"""
You are given a string S.
Your task is to print all possible combinations, up to size k,
  of the string in lexicographic sorted order.
Input: A single line containing the string S and integer value k separated by a space.
Output: Print the different combinations of string S on separate lines.

Just to mention, we implement list comprehension using double for.
Python parses the list from left to right.
Therefore, add the next loop to the end.

OUTER --> INNER
[c OUTSIDE_FOR INSIDE_FOR]
[c for b in a for c in b]
for b in a:
    for c in b:
        # have c
"""


from itertools import combinations


if __name__ == '__main__':
    STR, N = input().split()
    #for i in range(1, int(N) +1):
    #    for tuple in combinations(''.join(sorted(STR)), i):
    #        ''.join(tuple)
    print('\n'.join([''.join(tuple) for i in range(1, int(N) +1) for tuple in combinations(''.join(sorted(STR)), i)]))
