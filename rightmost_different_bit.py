class Solution:

    def posOfRightMostDiffBit(self, m, n):

        c = 0
        while (n > 0 or m > 0):
            c += 1
            if ((n % 2) != (m % 2)):
                return c
            n = n >> 1
            m = m >> 1
        return -1

def main():
    mn = [int(x) for x in input().strip().split()]
    m = mn[0]
    n = mn[1]
    ob = Solution()
    print(math.floor(ob.posOfRightMostDiffBit(m, n)))


if __name__ == "__main__":
    main()