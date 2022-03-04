class Solution:
    def canMakeTriangle(self, A, N):
        ans = []
        for i in range(0, N-2):

            if A[i] + A[i+1] > A[i+2] and A[i]+A[i+2] > A[i+1] and A[i+1]+A[i+2] > A[i]:
                ans.append(1)
            else:
                ans.append(0)
        return ans

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().strip().split()))
    ob = Solution()
    ans = ob.canMakeTriangle(A, N)
    for i in ans:
        print(i,end=" ")
    print()