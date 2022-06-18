class Solution:
    def isPalindrome(self, S):
        if S == S[::-1]:
            return 1
        else:
            return 0

if __name__ == '__main__':
    S = input()
    ob = Solution()
    answer = ob.isPalindrome(S)
    print(answer)