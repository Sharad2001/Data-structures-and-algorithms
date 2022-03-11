class Solution:
    def findHeight(self, N, arr):
        arr[0] = 1
        for i in range(1, N):
            arr[i] = arr[arr[i]] + 1
        return arr[N - 1]

if __name__ == '__main__':
    N = int(input())
    arr = input().split()
    for i in range(N):
        arr[i] = int(arr[i])

    ob = Solution()
    print(ob.findHeight(N, arr))
