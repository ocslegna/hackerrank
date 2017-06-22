#!/usr/bin/python3

"""
Given country stamps, print the number of distinct country stamps.
"""

if __name__ == '__main__':
    print(len(set([input() for n in range(int(input()))])))
