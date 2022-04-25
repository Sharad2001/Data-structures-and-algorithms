class Solution:
    def numOfPairs(self, X, Y, N):
        hmapx = {}
        hmapy = {}
        hmapxy = {}
        ans = 0
        for i in range(N):
            if X[i] in hmapx:
                ans += hmapx[X[i]]
                hmapx[X[i]] += 1
            else:
                hmapx[X[i]] = 1
            if Y[i] in hmapy:
                ans += hmapy[Y[i]]
                hmapy[Y[i]] += 1
            else:
                hmapy[Y[i]] = 1
            if str(X[i]) + "*" + str(Y[i]) in hmapxy:
                ans -= 2 * hmapxy[str(X[i]) + "*" + str(Y[i])]
                hmapxy[str(X[i]) + "*" + str(Y[i])] += 1
            else:
                hmapxy[str(X[i]) + "*" + str(Y[i])] = 1
        return ans

if __name__ == '__main__':
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    ob = Solution()
    print(ob.numOfPairs(X, Y, N))