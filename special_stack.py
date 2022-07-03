def push(arr, ele):
    arr.append(ele)


def pop(arr):
    arr.pop()

def isFull(n, arr):
    while n <= len(arr):
        if len(arr) == n:
            return True
        else:
            return False

def isEmpty(arr):
    if len(arr) == 0:
        return True
    else:
        return False

def getMin(n, arr):
    return min(arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    stack = []
    while (not isEmpty(stack)):
        pop(stack)

    for i in range(n):
        push(stack, arr[i])
    print(getMin(n, stack))