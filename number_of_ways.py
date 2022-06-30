class Solution:
    def arrangeTiles(self, N):
        dp = [0, 1, 1, 1, 2]
        if N <= 4:
            return dp[N]
        for i in range(5, N + 1):
            dp.append(dp[i - 4] + dp[i - 1])
        return dp[N]

if __name__ == '__main__':
    N = int(input())

    ob = Solution()
    print(ob.arrangeTiles(N))