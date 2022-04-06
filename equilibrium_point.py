class Solution:
    def equilibriumPoint(self, A, N):
        total_sum = sum(A)
        leftsum = 0
        for i, num in enumerate(A):
            total_sum -= num
            if leftsum == total_sum:
                return i+1
            leftsum += num
        return -1

import math
def main():
    N = int(input())

    A = [int(x) for x in input().strip().split()]
    ob = Solution()

    print(ob.equilibriumPoint(A, N))

if __name__ == "__main__":
    main()