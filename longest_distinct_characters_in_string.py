class Solution:

    def longestSubstrDistinctChars(self, S):
        max = 0
        for i in range(len(S)):
            substring = ""
            for e in S[i:]:
                if e not in substring:
                    substring += e
                else:
                    break

            len_substring = len(substring)
            if len_substring > max:
                max = len_substring
        return max

if __name__ == '__main__':
    S = input()

    solObj = Solution()

    ans = solObj.longestSubstrDistinctChars(S)

    print(ans)