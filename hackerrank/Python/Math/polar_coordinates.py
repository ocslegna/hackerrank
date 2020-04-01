#!/usr/bin/python3

"""
Task
  You are given a complex Z. Your task is to convert it to polar coordinates.

Input Format
  A single line containing the complex number Z. 
  Note: complex() function can be used in python to convert the input as a complex number.

Constraints
  Given number is a valid complex number.

Output Format
  Output two lines:
    The first line should contain the value of R.
    The second line should contain the value of PHI.

Sample Input
  1+2j

Sample Output
  2.23606797749979
  1.1071487177940904

Note: The output should be correct up to 3 decimal places.  
"""

import cmath

def get_polar_coordinates(COMPLEX_NUMBER):
    """ Get Polar Coordinates """
    PHI = cmath.phase(COMPLEX_NUMBER)
    if COMPLEX_NUMBER.imag == 0:
        R = abs(COMPLEX_NUMBER)
    else:
        R = cmath.sqrt(pow(COMPLEX_NUMBER.real, 2) + pow(COMPLEX_NUMBER.imag, 2))    

    return R, PHI


if __name__ == '__main__':
    COMPLEX_NUMBER = complex(input())

    R, PHI = get_polar_coordinates(COMPLEX_NUMBER)

    print(R.real)
    print(PHI)
    
