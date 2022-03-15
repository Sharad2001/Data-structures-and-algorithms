class Solution:
    def count(self, N, A, X):
        # code here
        ans = N
        for i in range(max(A).bit_length()):
            check = 1 << i
            if check & X:
                continue
            if check < X:
                check = X - (X%check) + check
            count = sum(1 for b in A if b & check != check)
            ans = min(ans, count)
        return ans
if __name__ == '__main__':
    N,X = map(int,input().strip().split())
    A = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.count(N, A, X)
    print(ans)
