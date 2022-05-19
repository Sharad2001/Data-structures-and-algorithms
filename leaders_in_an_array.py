class Solution:
    def leaders(self, A, N):
        ans = []
        ans.append(A[-1])
        for i in range(N - 2, -1, -1):
            if ans[-1] <= A[i]:
                ans.append(A[i])
        return reversed(ans)

import math
def main():
    N = int(input())
    A = [int(x) for x in input().strip().split()]
    obj = Solution()
    A = obj.leaders(A, N)
    for i in A:
        print(i, end=" ")
    print()
if __name__ == "__main__":
    main()