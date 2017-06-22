#!/usr/bin/python3

"""
In this challenge, the user enters a string and a substring.
Print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.
"""


def count_substring(string, sub_string):
    """ Count substrings """
    sslen = len(sub_string)
    slen = len(string)
    count = 0
    for i in range(0, slen - sslen + 1):
        if string[i: i + sslen] == sub_string:
            count += 1

    return count


if __name__ == '__main__':
    STR = input().strip()
    SUB_STR = input().strip()

    COUNT = count_substring(STR, SUB_STR)
    print(COUNT)
