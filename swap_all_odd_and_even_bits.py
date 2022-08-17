class Solution:

    def swapBits(self, n):
        b = bin(n)
        b = b[2:]
        if (len(b) % 2 == 1):
            b = "0" + b
        s = ""
        for i in range(0, len(b), 2):
            s += b[(i + 1)]
            s += b[i]
        return int(s, 2)

import math


def main():
    n = int(input())
    ob = Solution()
    print(ob.swapBits(n))

if __name__ == "__main__":
    main()