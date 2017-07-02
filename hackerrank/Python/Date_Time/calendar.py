#!/usr/bin/python3

"""
Get day from input
"""

import calendar

if __name__ == '__main__':
    DATE = list(map(int, input().split()))
    DAY = calendar.weekday(DATE[2], DATE[1], DATE[0])
    print(calendar.day_name[DAY].upper())
