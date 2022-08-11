class Solution:
    def isPowerofTwo(self, n):
        if n == 0:
            return False
        while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
        return True

import math


def main():
    n = int(input())
    ob = Solution()
    if ob.isPowerofTwo(n):
        print("YES")
    else:
        print("NO")



if __name__ == "__main__":
    main()