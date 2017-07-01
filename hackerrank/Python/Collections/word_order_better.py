#!/usr/bin/python3

"""
Input Format

The first line contains the integer, N.
The next N lines each contain a word.

Output Format

Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
"""

from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ == '__main__':
    OC = OrderedCounter(input() for _ in range(int(input())))
    print(len(OC))
    print(*OC.values())
