class Solution:
    def reverseWords(self, S):
        t = S.split(".")
        t.reverse()
        res = '.'.join(t)
        return res

if __name__ == '__main__':
    s = str(input())
    obj = Solution()
    print(obj.reverseWords(s))