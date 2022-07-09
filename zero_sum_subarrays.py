class Solution:
    def findSubArrays(self, arr, n):

        d = {}
        count = 0
        sum = 0
        for i in range(n):
            sum += arr[i]
            if sum == 0:
                count += 1
            count += d.get(sum, 0)
            d[sum] = d.get(sum, 0) + 1
        return count


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().strip().split(' ')]
    ob = Solution()
    print(ob.findSubArrays(A, N))