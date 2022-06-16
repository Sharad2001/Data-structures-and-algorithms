import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    exist = False
    while (True):
        if x1 == x2:
            exist= True
            break
        if (v1>v2 and x1> x2) or (v2>v1 and x2> x1) or (v1 == v2 and x1 != x2):
            break
        x1 += v1
        x2 += v2
    if exist:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    print(result)