class Solution:
    def getMinDiff(self, arr, n, k):
        if n == 1:
            return 0
        arr = sorted(arr)
        ans = arr[-1]-arr[0]
        smallest = arr[0] + k
        largest = arr[-1] - k
        for i in range(n-1):
            temp_min = min(smallest, arr[i+1]-k)
            temp_max = max(largest, arr[i]+k)
            if temp_min < 0:
                continue
            ans = min(ans, temp_max-temp_min)
        return ans

if __name__ == '__main__':
    k = int(input())
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.getMinDiff(arr, n, k)
    print(ans)