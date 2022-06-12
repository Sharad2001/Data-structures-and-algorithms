class Solution:

    def firstRepChar(self, s):
        t = set()
        for x in s:
            if x in t:
                return x
            t.add(x)
        return -1

if __name__ == '__main__':
        s = input()
        solObj = Solution()
        print(solObj.firstRepChar(s))