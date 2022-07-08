import atexit
import io
import sys
from collections import deque

class Solution:

    def max_of_subarrays(self, arr, n, k):
        i, j = 0, 0
        mx = max(arr[:k])
        ans = [mx]
        for i in range(k, n):
            if mx != arr[i - k]:
                mx = max(mx, arr[i])
            else:
                mx = max(arr[i - k + 1:i + 1])
            ans.append(mx)
        return ans

if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    res = ob.max_of_subarrays(arr, n, k)
    for i in range(len(res)):
        print(res[i], end=" ")
    print()