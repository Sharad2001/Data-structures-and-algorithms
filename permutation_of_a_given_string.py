class Solution:
    def find_permutation(self, S):
        ans = set()
        s = list(S)
        loop = len(S) * (len(S) - 1)

        while loop > 0:
            for i in range(len(s) - 1):
                s[i], s[i + 1] = s[i + 1], s[i]

                ans.add("".join(s))
                loop -= 1
        return sorted(ans)



if __name__ == '__main__':
    S = input()
    ob = Solution()
    ans = ob.find_permutation(S)
    for i in ans:
        print(i, end=" ")
    print()