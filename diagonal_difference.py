import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for i in range(0, len(arr)):
        sum1 = sum1 + arr[i][i]
    for j in range(0, len(arr)):
        sum2 = sum2 + arr[j][len(arr)-1-j]
    return abs(sum1 - sum2)
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)