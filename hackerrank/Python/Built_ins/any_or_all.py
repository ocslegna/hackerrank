#!/usr/bin/python3

"""
any or all

If all numbers are positive and any of them is palindrome, print True.
Otherwise, print False.
"""

if __name__ == '__main__':
    N = int(input())
    L = list(map(int, input().split()))
    if all([True if item > 0 else False for item in L]):
        """
        - We're checking if the string representation of item equals
         the inverted string representation of item.
        - The [::-1] slice takes care of inverting the string
        - After that, we compare for equality using ==.

        Another way: ''.join(reversed(item))
        """
        if any([True if str(item) == str(item)[::-1] else False for item in L]):
            print(True)
        else:
            print(False)
    else:
        print(False)
