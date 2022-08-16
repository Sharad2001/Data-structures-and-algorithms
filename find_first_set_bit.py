class Solution:

    def getFirstSetBit(self, n):
        for i in range(n):
            if ((1 << i) & n):
                return i + 1
        return 0


def main():
    n = int(input())
    ob = Solution()

    print(ob.getFirstSetBit(n))


if __name__ == "__main__":
    main()