from collections import Counter

class Solution:
    def relativeSort(self, A1, N, A2, M):
        res = []
        f = Counter(A1)
        for e in A2:
            res.extend([e] * f[e])
            f[e] = 0

        rem = list(sorted(filter(lambda x: f[x] != 0, f.keys())))

        for e in rem:
            res.extend([e] * f[e])
        return res

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    ob = Solution()
    a1 = ob.relativeSort(a1, n, a2, m)
    print(*a1, end=" ")

    print()