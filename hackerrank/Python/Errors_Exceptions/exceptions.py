#!/usr/bin/python3

"""
Task

You are given two values a and b.
Perform integer division and print a/b.

Input Format:
 The first line contains , the number of test cases.
 The next  lines each contain the space separated values of  and .

Output Format:
 Print the value of a/b.
 In the case of ZeroDivisionError or ValueError, print the error code.
"""

if __name__ == '__main__':    
    TESTCASES = int(input())
    for _ in range(TESTCASES):
        try:
            A, B = input().split()
            print(int(A) // int(B))
        except (ZeroDivisionError, ValueError) as ex:
            print("Error Code:", ex)