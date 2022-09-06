class Solution:
    def findMinSum(self, A,B,N):
        A.sort()
        B.sort()
        sum = 0
        for i in range(N):
            sum += abs(A[i] - B[i])
        return sum

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.findMinSum(A,B,N)
    print(ans)