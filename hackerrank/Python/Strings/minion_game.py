#!/usr/bin/python3

"""
Determine the winner of the game and their score
"""


def minion_game(string):
    """ Get count of vowels and consonants. """
    vowels = "AEIOU"
    kev_vc = 0
    stu_cc = 0
    for index, char in enumerate(string):
        if char in vowels:
            kev_vc += (len(string) - index)
        else:
            stu_cc += (len(string) - index)

    if kev_vc > stu_cc:
        print("Kevin " + str(kev_vc))
    elif kev_vc < stu_cc:
        print("Stuart " + str(stu_cc))
    else:
        print("Draw")


if __name__ == '__main__':
    STR = input()
    minion_game(STR)
