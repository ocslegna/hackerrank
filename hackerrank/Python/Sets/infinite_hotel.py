#!/usr/bin/python3

"""
Find the Captain's room number.
"""


from collections import Counter

if __name__ == '__main__':
    K = int(input())
    ROOM_NUMBER_LIST = list(map(int, input().split()))
    COUNT_LIST = Counter(ROOM_NUMBER_LIST)
    print(min(COUNT_LIST, key=COUNT_LIST.get))
