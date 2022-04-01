class Solution:
    def check(self, A, B, N):
        A1 = sorted(A)
        B1 = sorted(B)
        if A1 == B1:
            return 1
        else:
            return 0

if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
    B = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
    ob = Solution()
    if ob.check(A, B, N):
        print(1)
    else:
        print(0)
