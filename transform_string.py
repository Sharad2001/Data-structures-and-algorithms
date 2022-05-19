from collections import Counter


class Solution:
    def transform(self, A, B):
        if len(A) != len(B):
            return -1
        resA = Counter(A)
        resB = Counter(B)
        if resA != resB:
            return -1
        ans = 0
        i = len(A) - 1
        j = len(B) - 1
        while i >= 0 and j >= 0:
            if A[i] == B[j]:
                i -= 1
                j -= 1
            else:
                i -= 1
                ans += 1
        return ans

if __name__ == '__main__':
    line = input().strip().split()
    A = line[0]
    B = line[1]
    ob = Solution()
    print(ob.transform(A, B))