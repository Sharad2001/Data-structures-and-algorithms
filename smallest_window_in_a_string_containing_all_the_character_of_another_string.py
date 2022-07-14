from collections import defaultdict

import atexit
import io
import sys

class Solution:

    def smallestWindow(self, s, p):
        start = 0
        length = len(s) + 1
        a = ""
        dic1 = defaultdict(int)
        for i in p:
            dic1[i] += 1

        dic2 = defaultdict(int)
        l = len(p)
        c = 0
        for end in range(len(s)):
            dic2[s[end]] += 1
            if dic1[s[end]] >= dic2[s[end]] and dic2[s[end]] >= 1:
                c += 1
            while c == l:
                m = length
                length = min(length, end - start + 1)
                if length == end - start + 1 and m != length:
                    a = s[start:end + 1]
                dic2[s[start]] -= 1
                if dic1[s[start]] > dic2[s[start]]:
                    c = c - 1
                    if dic2[s[start]] == 0:
                        del dic2[s[start]]
                start = start + 1
        if a != "":
            return a
        return -1


if __name__ == '__main__':
    s = str(input())
    p = str(input())
    ob = Solution()
    print(ob.smallestWindow(s, p))