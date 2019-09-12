#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    text = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 21: "twenty one", 22: "twenty two", 23: "twenty three", 24: "twenty four", 25: "twenty five", 26: "twenty six", 27: "twenty seven", 28: "twenty eight", 29: "twenty nine"}
    if m == 0:
        return text[h] + " o' clock"
    elif m == 30:
        return "half past " + text[h]
    elif m < 30:
        if m == 15:
            return "quarter past " + text[h]
        if m == 1:
            return "one minute past " + text[h]
        else:
            return text[m] + " minutes past " + text[h]
    else:
        h+=1
        m = 60-m
        if m == 1:
            return "one minute to " + text[h]
        elif m == 15:
            return "quarter to " + text[h]
        else:
            return text[m] + " minutes to " + text[h]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
