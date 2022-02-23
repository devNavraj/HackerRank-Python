#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    kaprekar = []

    for i in range(p, q+1):
        square = str(i ** 2)
        n = len(square)

        if i == 1:
            kaprekar.append(i)
        elif n > 1 and i == int(square[:n//2]) + int(square[n//2:]):
            kaprekar.append(i)

    if len(kaprekar) == 0:
        print('INVALID RANGE')
    else:
        print(' '.join(str(x) for x in kaprekar))

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)


