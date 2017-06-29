#!/usr/bin/python3

"""
A counter is a container that stores elements as dictionary keys,
  and their counts are stored as dictionary values.

-The first line contains X, the number of shoes.
-The second line contains the space separated list
 of all the shoe sizes in the shop.
-The third line contains N, the number of customers.
-The next N lines contain the space separated values
  of the shoe size desired by the customer and Xi,
  the price of the shoe. (ShoeSize, Price)
"""


from collections import Counter


if __name__ == '__main__':
    NUMBER_SHOES = int(input())
    DICT_SHOES = Counter(map(int, input().split()))
    CUSTOMERS = int(input())
    MONEY_EARNED = []

    for i in range(CUSTOMERS):
        SIZE, PRICE = map(int, input().split())
        if DICT_SHOES[SIZE] > 0:
            DICT_SHOES.subtract(Counter([SIZE]))
            MONEY_EARNED.append(PRICE)

    print(sum(MONEY_EARNED))
