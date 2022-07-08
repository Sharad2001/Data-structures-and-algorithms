import heapq
import atexit
import io
import sys


class Solution:
    def heapify(self, arr, n, i):
        heapq.heapify(arr)

    def buildHeap(self, arr, n):
        heapq.heapify(arr)

    def HeapSort(self, arr, n):
        arr.sort()



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    Solution().HeapSort(arr, n)
    print(*arr)