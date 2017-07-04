#!/usr/bin/python3

"""
any or all

If all numbers are positive AND any of them is palindrome, print True.
Otherwise, print False.
"""

if __name__ == '__main__':
    N, L = int(input()), list(map(int, input().split()))
    """
    - We're checking if the string representation of item equals
        the inverted string representation of item.
    - The [::-1] slice takes care of inverting the string
    - After that, we compare for equality using ==.

    Another way: ''.join(reversed(item))
    """
    print(all([i > 0 for i in L]) and any([str(j) == str(j)[::-1] for j in L]))
