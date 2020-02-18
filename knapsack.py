#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the primeXor function below.
def primeXor(a):
    table = [[-1 for i in range(len(a) + 1)] for j in range(len(a) + 1)]

    table[0][0] = "X"

    for i in range(1, len(a) + 1):
        table[0][i] = a[i - 1]
    for i in range(1, len(a) + 1):
        table[i][0] = a[i - 1]

    values = [x for x in a]
    i = 1

    while i < len(table):
        c = 1
        while c < len(table):
            table[i][c] = table[i][c - 1] ^ table[0][c]
            if table[i][c] != 0:
                values.append(table[i][c])
            c += 1
            # print(i,c)
        i += 1

    for i in table:
        print(i)
    # print(values)
    count = 0
    for i in values:
        res = checkprime(i)
        count += res
    return count % (pow(10, 9) + 7)


def checkprime(n):
    # print(n)
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            # print(i)
            return 0
    # print(n)
    return 1


if __name__ == "__main__":

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = primeXor(a)
        print(result)
