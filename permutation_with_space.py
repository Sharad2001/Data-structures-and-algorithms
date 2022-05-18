class Solution:
    def permutation (self, S):
        n = len(S)
        ans = []
        def helper(ind, out):
            if ind == n:
                ans.append(out)
                return
            inp = " " + S[ind]
            inp1 = S[ind]
            helper(ind+1, out+inp)
            helper(ind+1, out+inp1)
        helper(1, S[0])
        return ans

if __name__ == '__main__':
    ob = Solution()
    S = input()
    ans = ob.permutation(S);
    write = "";
    for i in ans:
        write += "(" + i + ")"
    print(write)