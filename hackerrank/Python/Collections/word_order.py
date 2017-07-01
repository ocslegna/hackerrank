#!/usr/bin/python3

"""
"""

from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ == '__main__':
    STR, OC = "", OrderedCounter()
    for _ in range(int(input())):
        OC[''.join(input().splitlines())] += 1

    for k, v in OC.items():
        STR += str(v) + " "

    print(str(len(OC)) + "\n" + STR)