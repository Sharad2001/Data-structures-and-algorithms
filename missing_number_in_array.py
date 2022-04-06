class Solution:
    def MissingNumber(self, array, n):
        l1 = [i for i in range(1, n + 1)]
        s1 = set(array)
        s2 = set(l1)
        s3 = s2 - s1

        l2 = list(s3)
        return l2[0]

n = int(input())
a = list(map(int, input().split()))
s = Solution().MissingNumber(a, n)
print(s)