#!/usr/bin/python3

"""
You are the manager of a supermarket.
You have a list of N items together with their prices
 that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
If a new entry overwrites an existing entry,
 the original insertion position is left unchanged.

Input:
The first line contains the number of items, N.
The next N lines contains the item's name and price, separated by a space.

Output: Print the item_name and net_price in order of its first occurrence.

An ordered dictionary can be combined with the Counter class
 so that the counter remembers the order elements are first encountered:
"""


from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

if __name__ == '__main__':
    N = int(input())
    L = [tuple(' '.join(input().splitlines()).rsplit(' ', maxsplit=1)) for i in range(N)]
    OC = OrderedCounter()
    for k, v in L:
        OC[k] += int(v)

    for k, v in OC.items():
        print(k, v)
