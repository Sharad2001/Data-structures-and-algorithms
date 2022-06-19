class Solution:
    def shortestDistance(self, s, word1, word2):
        dict_1 = {word1:[], word2:[]}
        l = []
        for i in range(len(s)):
            if s[i] == word1:
                dict_1[word1].append(i)
            elif s[i] == word2:
                dict_1[word2].append(i)
        for i in range(len(dict_1[word1])):
            for j in range(len(dict_1[word2])):
                l.append(abs(dict_1[word1][i]-dict_1[word2][j]))
        return min(l)

if __name__ == '__main__':
    n = int(input())
    s = list(map(str,input().split()))
    word1 = input()
    word2 = input()
    ob = Solution()
    ans = ob.shortestDistance(s, word1, word2)
    print(ans)