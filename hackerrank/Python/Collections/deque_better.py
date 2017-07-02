#!/usr/bin/python3

"""
A deque is a double-ended queue.
It can be used to add or remove elements from both ends.

Deques support thread safe,
  memory efficient appends and pops from either side of
  the deque with approximately the same  performance in either direction.

Task:
 Perform append, pop, popleft and appendleft methods on an empty deque .

Input Format:
 The first line contains an integer N, the number of operations.
 The next N lines contains the space separated names of methods and their values.
"""


from collections import deque


if __name__ == '__main__':
    D = deque()
    for _ in range(int(input())):
        cmd, *args = input().split()
        getattr(D, cmd)(*args)

    print(*D)
