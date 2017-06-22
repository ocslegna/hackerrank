#!/usr/bin/python3

"""
Given a string s of length n.
Integer k such as k is a factor of n.
Split s in n/k substrings *subsegments* t_i of length k.
Then, use this subsegments to create u_i segments such that:
-Every character in u_i is in t_i.
-Any repeated ocurrence of a char is deleted from u_i
"""


def merge_the_tools(string, factor):
    """Print s/k subsegments u_i in t_i
        where repeated ocurrence of a char is deleted from u_i """
    lst = [string[n:n + factor] for n in range(0, len(string), factor)]
    for word in lst:
        letters = []
        new_word = []
        for letter in list(word):
            if letter not in letters:
                letters.append(letter)
                new_word.append(letter)

        print(''.join(new_word))


if __name__ == '__main__':
    STR, k = input(), int(input())
    merge_the_tools(STR, k)
