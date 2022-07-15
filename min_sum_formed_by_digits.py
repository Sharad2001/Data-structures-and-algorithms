import heapq as hq
class Solution:
    def minSum(self, arr, n):
        arr.sort()
        even = ""
        odd = ""
        for i in range(n):
            if i % 2 == 0:
                even += str(arr[i])
            else:
                odd += str(arr[i])
        if (even == ""):
            value = int(odd)
        elif (odd == ""):
            value = int(even)
        else:
            value = int(even) + int(odd)

        return value


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    ob = Solution()
    print(ob.minSum(arr, n))