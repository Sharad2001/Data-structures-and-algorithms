class Solution:
    def selectionSort(self, arr, n):
        for i in range(n-1):
            min_ind = i
            for j in range(i+1, n):
                if arr[j] < arr[min_ind]:
                    min_ind = j
            arr[min_ind], arr[i] = arr[i], arr[min_ind]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ob.selectionSort(arr, n)
    for i in range(n):
        print(arr[i], end=" ")
    print()