class Solution:
    def merge(self, arr, l, m, r):
        left = arr[l:m + 1]
        right = arr[m + 1: r + 1]
        i = 0
        j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                k += 1
                i += 1
            else:
                arr[k] = right[j]
                k += 1
                j += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        if r > l:
            m = (l + r) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)

import sys

input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    Solution().mergeSort(arr, 0, n - 1)
    for i in range(n):
        print(arr[i], end=" ")
    print()