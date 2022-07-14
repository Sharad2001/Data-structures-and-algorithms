class Solution:
    def findLongestConseqSubseq(self, arr, N):
        arrSet = set(arr)
        longest = 0
        for i in arr:
            if (i - 1) not in arrSet:
                length = 0
                while (i + length) in arrSet:
                    length += 1
                longest = max(longest, length)
        return longest


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(Solution().findLongestConseqSubseq(a, n))