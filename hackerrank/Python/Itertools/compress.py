#!/usr/bin/python3

"""
You are given a string S.
Suppose a character 'c' occurs consecutively X times in the string.
Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

Input Format:
A single line of input consisting of the string S.

Output Format:
A single line of output consisting of the modified string.

Groupby:
It generates a break or new group every time the value of the
 key function changes (which is why it is usually necessary
 to have sorted the data using the same key function).
"""


from itertools import groupby


if __name__ == '__main__':
    """
    Print each element of the generated list separated by a space
      where each element is a tuple (X,k)
      where X is the consecutively appearences of key k
    """

    print(*[(len(list(g)), int(k)) for k, g in groupby(input())], sep=' ')
