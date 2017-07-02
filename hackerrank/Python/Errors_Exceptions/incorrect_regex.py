#!/usr/bin/python3

"""
You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format:
 The first line contains integer T, the number of test cases.
 The next T lines contains the string S.

Output Format:
 Print "True" or "False" for each test case without quotes.

Sample Input:
 2
 .*\+
 .*+

Sample Output:
 True
 False
"""

import re


if __name__ == '__main__':
    for _ in range(int(input())):
        try:
            print(bool(re.compile(input())))
        except re.error:
            print(False)