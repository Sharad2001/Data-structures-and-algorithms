# User function Template for python3
from bisect import bisect as bi
import atexit
import io
import sys

class Solution:
    def countPairs(self, a, b, M, N):
        a.sort()
        b.sort()
        ans = 0
        for x in a:
            if x == 1:
                continue
            elif x == 2:
                ans += bi(b, 1) + N - bi(b, 4)
            elif x == 3:
                ans += bi(b, 2) + N - bi(b, 3)
            else:
                ans += bi(b, 1) + N - bi(b, x)
        return ans


if __name__ == '__main__':
    M, N = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    ob = Solution();
    print(ob.countPairs(a, b, M, N))