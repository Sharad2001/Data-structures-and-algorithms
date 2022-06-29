class Solution:
    def minJumps(self, arr, n):
        temp = arr[0]
        for i in range(n):
            if arr[i] < temp:
                arr[i] = temp -1
                temp = arr[i]
            else:
                temp = arr[i]
        arr[n-1] = 0
        for i in range(n-2, -1, -1):
            if arr[i] >= n-1-i:
                arr[i] = 1
            elif arr[i] + i <= n-1 and arr[i] != 0:
                arr[i] = arr[arr[i] + i] +1
            else:
                return -1
        return arr[0]

if __name__ == '__main__':
    n = int(input())
    Arr = [int(x) for x in input().split()]
    ob = Solution()
    ans = ob.minJumps(Arr,n)
    print(ans)