def push1(a, x):
    i = 0
    while a[i] != -1:
        i += 1
    a[i] = x

def push2(a, x):
    a.append(x)

def pop1(a):
    i = 0
    while a[i] != -1:
        i += 1
    if i > 0:
        x = a[i - 1]
        a[i - 1] = -1
        return x
    return -1


def pop2(a):
    if a[-1] != -1:
        return a.pop()
    return -1

import atexit
import io
import sys

top2 = 101
top1 = -1

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    a = [-1 for i in range(101)]
    i = 0
    while i < len(arr):
        if arr[i] == 1:
            if arr[i + 1] == 1:
                push1(a, arr[i + 2])
                i += 1
            else:
                print(pop1(a), end=" ")
            i += 1
        else:
            if arr[i + 1] == 1:
                push2(a, arr[i + 2])
                i += 1
            else:
                print(pop2(a), end=" ")
            i += 1
        i += 1
    top2 = 101
    top1 = -1
    print(' ')