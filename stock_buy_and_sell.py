class Solution:
    def stockBuySell(self, A, n):
        l, r = 0, 0
        li = []

        while (r < n - 1):
            if (A[r] < A[r + 1]):
                r += 1
            else:
                if (l < r):
                    li.append([l, r])
                r += 1
                l = r
        if (l < r):
            li.append([l, r])
        return li

def check(ans, A, p):
    c = 0
    for i in range(len(ans)):
        c += A[ans[i][1]] - A[ans[i][0]]
    if (c == p):
        return 1
    else:
        return 0

if __name__ == '__main__':
    n = int(input())
    A = [int(x) for x in input().strip().split()]
    ob = Solution()
    ans = ob.stockBuySell(A, n)
    p = 0
    for i in range(n - 1):
        p += max(0, A[i + 1] - A[i])
    if (len(ans) == 0):
        print("No Profit", end="")
    else:
        print(check(ans, A, p), end="")
    print()