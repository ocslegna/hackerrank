#!/usr/bin/python3

"""
Format i decimals in octal, hexa and bin with proper len(bin(i)) spaced_padded.
"""


def print_formatted(number):
    """ print_formatted """
    spaced_padded = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(str(i).rjust(spaced_padded) + str(
            oct(i))[2:].rjust(spaced_padded + 1) + str(
                hex(i)[2:]).upper().rjust(spaced_padded + 1) + str(
                    bin(i)[2:]).rjust(spaced_padded + 1))


if __name__ == '__main__':
    N = int(input())
    print_formatted(N)
