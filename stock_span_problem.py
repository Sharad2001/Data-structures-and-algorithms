class Solution:

    def calculateSpan(self, a, n):
        stack = []
        ans = []
        for i in range(n):
            if len(stack) == 0:
                ans.append(-1)
            elif len(stack) > 0:
                while len(stack) > 0 and stack[-1][0] <= a[i]:
                    stack.pop()
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack[-1][1])
            stack.append([a[i], i])
        for i in range(n):
            ans[i] = i - ans[i]
        return ans

import atexit
import io
import sys

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    obj = Solution()
    ans = obj.calculateSpan(a, n);
    for i in range(n):
        print(ans[i], end=" ")
    print()