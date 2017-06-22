#!/usr/bin/python3

""" Print full name """


def print_full_name(first_name, last_name):
    """ Print full name """
    print("Hello " + first_name + " " + last_name +
          "! You just delved into python.")


if __name__ == '__main__':
    FIRST_NAME = input()
    LAST_NAME = input()
    print_full_name(FIRST_NAME, LAST_NAME)
