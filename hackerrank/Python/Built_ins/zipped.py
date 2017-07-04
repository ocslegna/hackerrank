
#!/usr/bin/python3

"""
zip():
This function returns a list of tuples.
The ith tuple contains the ith element from each of the argument sequences or iterables.
If the argument sequences are of unequal lengths,
 then the returned list is truncated to the length of the shortest argument sequence.

>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]

>>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]

>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>>
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]
__

Task:
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

Input:
 The first line contains N and X separated by a space.
 The next X lines contains the space separated marks obtained
  by students in a particular subject.

Output Format:
 Print the averages of all students on separate lines.
 The averages must be correct up to 1 decimal place.

_
In other words:
 NxM list -> Mxmin(N) when zipped
"""

from decimal import Decimal

if __name__ == '__main__':
    N, X = map(int, input().split())
    NOTES = [list(map(Decimal, input().split())) for _ in range(X)]
    ZPP = zip(*NOTES)
    for tuple in ZPP:
        AVERAGE = sum(map(float, tuple)) / len(tuple)
        print("%.1f" % AVERAGE)