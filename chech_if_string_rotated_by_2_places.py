class Solution:
    def isRotated(self, str1, str2):
        n = len(str1)
        a = str1[2:] + str1[:2]
        b = str1[-2] + str1[-1] + str1[0:n - 2]

        if (a == str2 or b == str2):
            return True
        else:
            return False

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
    s = str(input())
    p = str(input())
    if (Solution().isRotated(s, p)):
        print(1)
    else:
        print(0)