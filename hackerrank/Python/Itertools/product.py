#!/usr/bin/python3

"""
You are given a two lists A and B. Your task is to compute their cartesian product X.
Examples:
  print list(product([1,2,3],repeat = 2))
  print list(product([1,2,3],[3,4]))
  print list(product(*A))
  print list(product(*B))
"""


from itertools import product


if __name__ == '__main__':
    A, B = list(map(int, input().split())), list(map(int, input().split()))
    print(*[tuple for tuple in list(product(A, B))], sep=' ', end=' ')
