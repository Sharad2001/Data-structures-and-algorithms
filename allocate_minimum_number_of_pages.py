class Solution:

    def findPages(self, A, N, M):

        if (N == 0):
            return -1
        if (N == 1 and M == 1):
            return A[0]
        if (N < M):
            return -1
        res = None
        low, high = max(A), sum(A)

        while (low <= high):
            mid = low + (high - low) // 2
            if (self.isPartitionValid(arr, low, mid, high, n, M)):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res

    def isPartitionValid(self, arr, low, mid, high, n, M):
        i = pageSum = 0
        studentCount = 1
        while (i < n):
            pageSum += arr[i]
            if (pageSum > mid):
                studentCount += 1
                pageSum = arr[i]
            if (studentCount > M):
                return False
            i += 1
        return True


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    m = int(input())
    ob = Solution()
    print(ob.findPages(arr, n, m))