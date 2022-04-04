class Solution:

    def zigZag(self,arr, n):
        flag = True
        for i in range(n-1):
            if flag is True:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            flag = bool(1-flag)
        return arr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ob.zigZag(arr, n)
    for x in arr:
        print(x, end=" ")
    print()