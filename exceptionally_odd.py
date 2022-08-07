class Solution:
    def getOddOccurrence(self, arr, n):
        res = 0
        for i in arr:
            res = res ^ i
        return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.getOddOccurrence(arr, n)
    print(ans)