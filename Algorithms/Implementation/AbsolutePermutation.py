#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    a = list(i+1 for i in range(n))
    i=0
    if k==0:
        return(a)
    if n%2 != 0:
        return([-1])
    if n % (k*2) == 0:
        while(i<len(a)):
            for _ in range(k):
                a[i], a[i+k] = a[i+k], a[i]
                i+=1
            i = i+k
    else:
        return([-1])
    return(a)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
