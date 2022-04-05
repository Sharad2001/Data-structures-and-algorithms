class Solution:
    def subArraySum(self, arr, n, s):
        Sum = arr[0]
        first = 0
        last = 0
        while first < n and last < n:
            if Sum == s:
                return first + 1, last + 1
            elif Sum < s and last < n - 1:
                last += 1
                Sum += arr[last]
            else:
                Sum -= arr[first]
                first += 1
        return [-1]

import math
def main():
    NS = input().strip().split()
    N = int(NS[0])
    S = int(NS[1])

    A = list(map(int, input().split()))
    ob = Solution()
    ans = ob.subArraySum(A, N, S)

    for i in ans:
        print(i, end=" ")

    print()


if __name__ == "__main__":
    main()