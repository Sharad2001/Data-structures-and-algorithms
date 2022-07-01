class Solution:
    def peakElement(self, arr, n):
        def binarySearch(left, right, arr):
            mid = ((left + right) // 2)
            if left >= right:
                return left
            if arr[mid] < arr[mid + 1]:
                return binarySearch(mid + 1, right, arr)
            else:
                return binarySearch(left, mid, arr)

        return binarySearch(0, n - 1, arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    index = Solution().peakElement(arr.copy(), n)
    flag = False
    if index < 0 or index >= n:
        flag = False
    else:
        if index == 0 and n == 1:
            flag = True
        elif index == 0 and arr[index] >= arr[index + 1]:
            flag = True
        elif index == n - 1 and arr[index] >= arr[index - 1]:
            flag = True
        elif arr[index - 1] <= arr[index] and arr[index] >= arr[index + 1]:
            flag = True
        else:
            flag = False

    if flag:
        print(1)
    else:
        print(0)