#!/usr/bin/python3

"""
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters,
alphabetical characters, DIGITS, lowercase and uppercase characters.
"""

"""
str = input()
print any(c.isalnum()  for c in str)
print any(c.isalpha() for c in str)
print any(c.isdigit() for c in str)
print any(c.islower() for c in str)
print any(c.isupper() for c in str)
"""


if __name__ == '__main__':
    S = input()
    ANUM = False
    ABET = False
    DIGITS = False
    LOWER = False
    UPPER = False

    for c in S:
        if not ANUM and c.isalnum():
            ANUM = True
        if not ABET and c.isalpha():
            ABET = True
        if not DIGITS and c.isdigit():
            DIGITS = True
        if not LOWER and c.islower():
            LOWER = True
        if not UPPER and c.isupper():
            UPPER = True

    print(ANUM)
    print(ABET)
    print(DIGITS)
    print(LOWER)
    print(UPPER)
