#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(a, b):
    digits = 1 + math.floor(math.log10(a))
    lower = a
    kaps = []
    while True:
        power = 10**digits
        upper = min(b+1, power)
        for n in range(lower, upper):
            l, r = divmod(n**2, power)
            if l+r == n:
                kaps.append(n)
        if n == b:
            break
        digits += 1
        lower = upper
    if kaps:
        print(*kaps)
    else:
        print('INVALID RANGE')
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
