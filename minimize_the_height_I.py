class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        res = arr[-1]-arr[0]
        for i in range(1, n):
            minn = min(arr[0]+k, arr[i]-k)
            maxx = max(arr[-1]-k, arr[i-1]+k)
            res = min(res, maxx-minn)
        return res

if __name__ == '__main__':
    k = int(input())
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.getMinDiff(arr, n, k)
    print(ans)