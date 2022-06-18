class Solution:
    def isMatching(self, a, b):
        if (a == "(" and b == ")") or \
                (a == "{" and b == "}") or \
                (a == "[" and b == "]"):
            return True
        else:
            return False

    def ispar(self, x):
        stack = []
        for i in x:
            if i in ('(', "{", "["):
                stack.append(i)
            else:
                if not stack:
                    return False
                elif self.isMatching(stack[-1], i) == False:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        else:
            return True

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
    obj = Solution()
    if obj.ispar(s):
        print("balanced")
    else:
        print("not balanced")