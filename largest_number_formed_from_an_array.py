import functools


def my_cmp_f(a, b):
    if a + b < b + a:
        return -1
    if a + b > b + a:
        return 1
    return 0

class Solution:

    def printLargest(self, arr):
        arr = [str(elem) for elem in arr]
        arr = sorted(arr, reverse=True)
        arr = sorted(arr, reverse=True, key=functools.cmp_to_key(my_cmp_f))

        result = ''.join(arr)
        return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(str, input().strip().split()))
    ob = Solution()
    ans = ob.printLargest(arr)
    print(ans)