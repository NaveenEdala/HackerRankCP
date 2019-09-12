#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    currentlevel = 0
    for letter in s:
        if letter=="U":
            currentlevel += 1
        else:
            currentlevel -= 1
        if currentlevel==0 and letter=="U":
            valleys += 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
