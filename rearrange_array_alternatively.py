class Solution:
    def rearrange(self, arr, n):
        low = 0
        high = n - 1
        temp = n * [None]
        flag = True
        for i in range(n):
            if flag is True:
                temp[i] = arr[high]
                high -= 1
            else:
                temp[i] = arr[low]
                low += 1
            flag = bool(1 - flag)

        for i in range(n):
            arr[i] = temp[i]
        return arr

import math

def main():

    n = int(input())

    arr = [int(x) for x in input().strip().split()]

    ob = Solution()
    ob.rearrange(arr, n)

    for i in arr:
        print(i, end=" ")

    print()


if __name__ == "__main__":
    main()