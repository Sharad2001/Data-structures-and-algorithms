def sumOfMaxandMin(arr, n):

    mini = arr[0]
    maxi = arr[0]

    for i in range(len(arr)):
        if arr[i] < mini:
            mini = arr[i]
        if arr[i] > maxi:
            maxi = arr[i]
    return (maxi + mini)
if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    print(sumOfMaxandMin(arr, n))