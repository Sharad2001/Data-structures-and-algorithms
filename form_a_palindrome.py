class Solution:
    def countMin(self, Str):
        n = len(Str)
        table = [[0 for i in range(n)] for i in range(n)]

        for gap in range(1, n):
            l = 0
            for h in range(gap, n):
                if Str[l] == Str[h]:
                    table[l][h] = table[l + 1][h - 1]
                else:
                    table[l][h] = min(table[l][h - 1], table[l + 1][h]) + 1
                l += 1
        return table[0][n - 1]

if __name__ == '__main__':
    Str = input()

    solObj = Solution()

    print(solObj.countMin(Str))