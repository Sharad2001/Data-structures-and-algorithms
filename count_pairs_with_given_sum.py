class Solution:
    def getPairsCount(self, arr, n, k):
        count = 0
        s = {}
        for i in arr:
            c = k - i
            if c in s:
                count += s[c]
            s[i] = s.get(i, 0)+1
        return count

if __name__ == '__main__':
    n, k = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.getPairsCount(arr, n, k)
    print(ans)