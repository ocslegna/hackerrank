#!/usr/bin/python3

"""
You are given a string S.
S contains alphanumeric characters only.

Your task is to sort the string S in the following manner:
 All sorted lowercase letters are ahead of uppercase letters.
 All sorted uppercase letters are ahead of digits.
 All sorted odd digits are ahead of sorted even digits.

Input Format:
 A single line of input contains the string S.

Output Format:
 Output the sorted string S.

Sample Input:
 Sorting1234

Sample Output:
 ginortS1324

Note:
a) Using join, for or while anywhere in your code,
 even as substrings, will result in a score of 0.
b) You can only use  sorted function in your code.
 A 0 score will be awarded for using sorted more than once.

Hint: Success is not the key, but  is success.
"""

if __name__ == '__main__':
    print(*sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x)), sep = '')

