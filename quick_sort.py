class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.quickSort(arr, low, p)
            self.quickSort(arr, p + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    Solution().quickSort(arr, 0, n - 1)
    for i in range(n):
        print(arr[i], end=" ")
    print()