#!/usr/bin/python3

"""
fib with map and lambda
"""

cube = lambda x: x ** 3

def fibonacci(n):
    """ return list of fibonicci numbers. """
    a, b, c = 0, 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    N = int(input())
    print(list(map(cube, fibonacci(N))))
