#!/usr/bin/python3

"""
You are given a partial code that is used for generating the HackerRank
Logo of variable T_NESS.
Your task is to replace the blank (______) with rjust, ljust or center.
"""

if __name__ == '__main__':

    # Replace all ______ with rjust, ljust or center.
    T_NESS = int(input())  # This must be an odd number
    C = 'H'

    # Top Cone
    for i in range(T_NESS):
        print((C * i).rjust(T_NESS - 1) + C + (C * i).ljust(T_NESS - 1))

    # Top Pillars
    for i in range(T_NESS + 1):
        print((C * T_NESS).center(T_NESS * 2) +
              (C * T_NESS).center(T_NESS * 6))

    # Middle Belt
    for i in range((T_NESS + 1) // 2):
        print((C * T_NESS * 5).center(T_NESS * 6))

    # Bottom Pillars
    for i in range(T_NESS + 1):
        print((C * T_NESS).center(T_NESS * 2) +
              (C * T_NESS).center(T_NESS * 6))

    # Bottom Cone
    for i in range(T_NESS):
        print(((C * (T_NESS - i - 1)).rjust(T_NESS) + C +
               (C * (T_NESS - i - 1)).ljust(T_NESS)).rjust(T_NESS * 6))
