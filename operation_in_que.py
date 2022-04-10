class Solution:
    def enqueue(self, q, x):
        q.append(x)

    def dequeue(self, q):
        q.pop(0)

    def front(self, q):
        return q[0]

    def find(self, q, x):
        return x in q

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
    a = list(map(str, input().strip().split()))
    queue = []
    ob = Solution()
    i = 0
    while i < len(a):
        if a[i] == 'i':
            ob.enqueue(queue, a[i + 1])
            i += 1
        elif a[i] == 'f':
            if (ob.find(queue, a[i + 1])):
                print("Yes")
            else:
                print("No")
            i += 1
        elif a[i] == 'r':
            (ob.dequeue(queue))
        else:
            print(ob.front(queue))
        i += 1