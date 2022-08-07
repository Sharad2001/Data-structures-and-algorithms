class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        dp = [[0 for i in range(m + 1)] for j in range(2)]
        res = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if (S1[i - 1] == S2[j - 1]):
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                    if (dp[i % 2][j] > res):
                        res = dp[i % 2][j]
                else:
                    dp[i % 2][j] = 0
        return res

if __name__ == '__main__':
    n, m = input().strip().split(" ")
    n, m = int(n), int(m)
    S1 = input().strip()
    S2 = input().strip()

    ob = Solution()
    print(ob.longestCommonSubstr(S1, S2, n, m))