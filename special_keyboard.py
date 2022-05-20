class Solution:
    def findTime(self, S1, S2):
        time = 0
        ind = 0
        for i in S2:
            a = S1.index(i)
            time = time + abs(a - ind)
            ind = a
        return time

if __name__ == '__main__':
    S1 = input()
    S2 = input()
    ob = Solution()
    print(ob.findTime(S1, S2))