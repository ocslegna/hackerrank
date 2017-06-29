#!/usr/bin/python3

"""
In this challenge, you will be given 2 integers, n and m.
There are n words, which might repeat, in word group A.
There are m words belonging to word group B.
For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A.
If it does not appear, print -1.

Input:
  The first line contains integers, n and m separated by a space.
  The next n lines contains the words belonging to group A.
  The next m lines contains the words belonging to group B.
Output:
  M lines.
  The ith line should contain the 1-indexed positions of the
    occurrences of the ith word separated by spaces.
"""


from collections import defaultdict


if __name__ == '__main__':
    D = defaultdict(list)
    N, M = map(int, input().split())
    A = [(input(), str(i+1)) for i in range(N)]
    for word, index in A:
        D[word].append(index)

    for i in range(M):
        # If does not exists, returns -1 otherwise the object_list.
        values = D.get(input(), -1)
        if values == -1:
            print(values)
        else:
            print(' '.join(values))
