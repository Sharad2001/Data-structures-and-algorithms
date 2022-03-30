def calculate(arr, n):
    res = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] ^ arr[j] == 0:
                res += 1
    return res

n = int(input())
arr = list(map(int, input().strip().split()))
res = calculate(arr, n)
print(res)