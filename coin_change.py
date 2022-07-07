import sys
sys.setrecursionlimit(10 ** 6)

class Solution:
    def count(self, S, m, n):
        t = [0 for k in range(n+1)]
        t[0] = 1
        for i in range(0, m):
            for j in range(S[i], n+1):
                t[j] += t[j-S[i]]
        return t[n]


if __name__ == '__main__':
    n,m = list(map(int, input().strip().split()))
    S = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.count(S,m,n))