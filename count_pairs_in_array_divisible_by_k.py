class Solution:
    def countKdivPairs(self, arr, n, k):
        counter = [0] * k
        ans = 0

        for i in arr:
            i %= k
            ans += counter[(k - i) % k]
            counter[i] += 1

        return ans

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    k = int(input())
    ob = Solution()
    print(ob.countKdivPairs(a, n, k))