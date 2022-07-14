import atexit
import io
import sys
class Solution:
    def minIndexChar(self, Str, pat):
        d = {}
        for i in Str:
            d[i] = 1
        for j in pat:
            d[j] = 2
        for i in range(len(Str)):
            if d[Str[i]] == 2:
                return i
        return -1


if __name__ == '__main__':
        s = str(input())
        p = str(input())
        obj = Solution()
        ans = obj.minIndexChar(s, p)
        print(ans)