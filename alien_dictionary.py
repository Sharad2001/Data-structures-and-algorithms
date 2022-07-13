class Solution:
    def findOrder(self, dict, N, K):
        adj = {c: set() for w in dict for c in w}
        for i in range(len(dict) - 1):
            w1, w2 = dict[i], dict[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return ''.join(res)

class sort_by_order:
    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)

if __name__ == '__main__':
    line = input().strip().split()
    n = int(line[0])
    k = int(line[1])

    alien_dict = [x for x in input().strip().split()]
    duplicate_dict = alien_dict.copy()
    ob = Solution()
    order = ob.findOrder(alien_dict, n, k)
    s = ""
    for i in range(k):
        s += chr(97 + i)
    l = list(order)
    l.sort()
    l = "".join(l)
    if s != l:
        print(0)
    else:
        x = sort_by_order(order)
        x.sort_this_list(duplicate_dict)

        if duplicate_dict == alien_dict:
            print(1)
        else:
            print(0)