class Solution:
    def reverseInGroups(self, arr, N, K):

        for i in range(0, N, K):
            K = min(K, N - i)
            for j in range(K // 2):
                arr[i + j], arr[i + K - 1 - j] = arr[i + K - 1 - j], arr[i + j]

import math
def main():
    nk = [int(x) for x in input().strip().split()]
    N = nk[0]
    K = nk[1]
    arr = [int(x) for x in input().strip().split()]

    ob = Solution()
    ob.reverseInGroups(arr, N, K)
    for i in arr:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    main()
