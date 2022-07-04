class Solution:
    def minVal(self, a, b):
        one = bin(b).count("1")
        ans = 0
        bit = 1 << 29
        while one > 0 and bit > 0:
            if a & bit:
                ans |= bit
                one -= 1
            bit >>= 1

        bit = 1
        while one > 0 and bit <= 1 << 29:
            if ans & bit == 0:
                ans |= bit
                one -= 1
            bit <<= 1
        return ans


import atexit
import io
import sys

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    ob = Solution()
    print(ob.minVal(a, b))