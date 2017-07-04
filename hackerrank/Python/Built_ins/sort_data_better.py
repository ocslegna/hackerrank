#!/usr/bin/python3

"""
You are given data in a tabular format.
The data contains N rows, and each row contains M space separated elements.
You can imagine the M items to be different attributes,
 (like height, weight, energy, etc.) and each of the N rows as an instance or a sample.

Your task is to sort the table on the Kth attribute and print the final resulting table.
Note: If two attributes are the same for different rows,
 print the row that appeared first in the input.
__

Input Format:
 The first line contains N and M separated by a space.
 The next N lines each contain M elements.
 The last line contains K.

Output Format:
 Print the N lines of the sorted table.
 Each line should contain the space separated elements.
 Check the sample below for clarity.

Sample Input
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
"""

if __name__ == '__main__':
    """ Sorting the rows without fully parsing them (to ints), only parsing the K-th elements: 
    """
    N, M = map(int, input().split())
    LIST_ELEMENTS = [input() for _ in range(N)]
    ORDER = int(input())
    for line in sorted(LIST_ELEMENTS, key=lambda row: int(line.split()[ORDER])):
        print(line)
