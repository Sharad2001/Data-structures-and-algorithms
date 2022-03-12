class Solution:
    def bubbleSort(self, arr, n):
        for i in range(n-1):
            swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if swapped == False:
                return

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ob.bubbleSort(arr, n)
    for i in arr:
        print(i, end = " ")
    print()