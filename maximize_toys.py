class Solution:
    def toyCount(self, N, K, arr):
        arr.sort()
        count = 0
        for i in range(N):
            if (arr[i] <= K):
                count += 1
            K = K - arr[i]
        return count


if __name__ == '__main__':
    N, K = [int(x) for x in input().split()]
    arr = input().split()
    for it in range(N):
        arr[it] = int(arr[it])

    ob = Solution()
    print(ob.toyCount(N, K, arr))