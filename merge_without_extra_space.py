class Solution:
    def merge(self, arr1, arr2, n, m):
        i = 0
        j = 0
        k = n - 1
        while i <= k and j < m:
            if arr1[i] < arr2[j]:
                i += 1
            else:
                temp = arr2[j]
                arr2[j] = arr1[k]
                arr1[k] = temp
                j += 1
                k -= 1
        arr1.sort()
        arr2.sort()


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    arr1 = list(map(int, input().strip().split()))
    arr2 = list(map(int, input().strip().split()))
    ob = Solution()
    ob.merge(arr1, arr2, n, m)
    print(*arr1, end=" ")
    print(*arr2)