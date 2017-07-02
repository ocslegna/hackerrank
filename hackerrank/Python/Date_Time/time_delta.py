#!/usr/bin/python3

"""
Task
Given 2 timestamps, print the absolute difference
 (in seconds) between them.

Input Format
The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t_1 and time t_2.

Output Format
Print the absolute difference (t_1 - t_2) in seconds.
"""

from datetime import datetime as dt


if __name__ == '__main__':
    FORMAT = '%a %d %b %Y %H:%M:%S %z'
    for i in range(int(input())):
        print(int(abs((dt.strptime(input(), FORMAT) -
                       dt.strptime(input(), FORMAT)).total_seconds())))
