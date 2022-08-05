class Solution:
    def editDistance(self, s, t):
        m = len(s)
        n = len(t)
        dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        return dp[m][n]

if __name__ == '__main__':
    s, t = input().split()
    ob = Solution();
    ans = ob.editDistance(s, t)
    print(ans)