class Solution:
    def search(self, patt, s):
        li = []
        x = s.find(patt)
        length = len(patt)
        if x == -1:
            return ['-1']

        for i in range(len(s) - length + 1):
            li.append(s[i:length])
            length = length + 1

        ans = []
        for i in range(len(li)):
            if li[i] == patt:
                ans.append(i + 1)
        return ans

if __name__ == '__main__':
    s = input().strip()
    patt = input().strip()
    ob = Solution()
    ans = ob.search(patt, s)
    for value in ans:
        print(value, end=' ')
    print()