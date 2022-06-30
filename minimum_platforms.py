class Solution:
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        res, j = 1, 0
        for i in range(1, n):
            if dep[j] >= arr[i]:
                res += 1
            else:
                j += 1
        return res

import atexit
import io
import sys

if __name__ == '__main__':
    n = int(input())
    arrival = list(map(int, input().strip().split()))
    departure = list(map(int, input().strip().split()))
    ob=Solution()
    print(ob.minimumPlatform(n,arrival,departure))