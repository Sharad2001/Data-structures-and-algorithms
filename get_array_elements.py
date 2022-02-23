class Solution:
    def printArrayRecursively(self, arr, n):
        if n <= 0:
            return
        self.printArrayRecursively(arr, n - 1)
        print(arr[n - 1], end=" ")
if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    ob = Solution()
    ob.printArrayRecursively(arr, n)
    print()