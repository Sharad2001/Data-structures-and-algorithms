class Solution:
    def removeDups(self, S):
        res = ""
        for i in S:
            if i not in res:
                res += i
        return res

if __name__ == '__main__':
    s = input()

    ob = Solution()
    answer = ob.removeDups(s)

    print(answer)