#!/usr/bin/python3

"""
Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

Named tuples are especially useful for assigning field
 names to result tuples returned by the csv or sqlite3 modules:

__
DATA is a STUDENT list that takes as arguments those returned
 by the * operator when applying a resulting list of splitting the input.
"""


from collections import namedtuple


if __name__ == '__main__':
    STUDENTS = int(input())
    STUDENT = namedtuple('STUDENT', input())
    DATA = [STUDENT(*input().split()) for i in range(STUDENTS)]
    print(sum(int(stud.MARKS) for stud in DATA)/STUDENTS)
