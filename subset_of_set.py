class Solution:
    def subsets(self, A):
        # code here
        if len(A) == 0:
            return []
        res = [[]]
        for val in A:
            n = len(res)
            for i in range(n):
                x = res[i] + [val]
                res.append(x)
        return sorted(res)
if __name__ == '__main__':
    A = list(map(int, input().strip().split()))

    ob = Solution()
    result = ob.subsets(A)

    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end=" ")

        print()
