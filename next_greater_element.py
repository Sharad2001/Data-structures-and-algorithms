class Solution:
    def nextLargerElement(self,arr,n):
        stack = []
        ans = []
        for i in range(n-1, -1, -1):
            if len(stack) == 0:
                ans.append(-1)
            elif len(stack) >0 and stack[-1] > arr[i]:
                ans.append(stack[-1])
            elif len(stack) > 0 and arr[i] >= stack[-1]:
                while len(stack) > 0 and arr[i] >= stack[-1]:
                    stack.pop()
                if len(stack) > 0:
                    ans.append(stack[-1])
                else:
                    ans.append(-1)
            stack.append(arr[i])
        return ans[::-1]

import atexit
import io
import sys


if __name__ == '__main__':
    n = int(input())

    a = list(map(int,input().strip().split()))
    obj = Solution()
    res = obj.nextLargerElement(a,n)
    for i in range (len (res)):
        print (res[i], end = " ")
    print ()