class Solution:
    def wordBreakUtil(self, dictionary, sent, result, string):
        if string == "":
            result.append(" ".join(sent))
        for i in range(1, len(string) + 1):
            if string[:i] in dictionary:
                new_sent = sent[:]
                new_sent.append(string[:i])
                self.wordBreakUtil(dictionary, new_sent, result, string[i:])

    def wordBreak(self, n, dict, s):

        result = []
        dictionary = set(dict)
        self.wordBreakUtil(dictionary, [], result, s)
        return result

if __name__ == '__main__':
    n = int(input())
    dict = input().split()
    s = input()

    ob = Solution()
    ans = ob.wordBreak(n, dict, s)
    if (len(ans) == 0):
        print("Empty")
    else:
        ans.sort()
        for it in (ans):
            print("(" + it, end=")")
        print()