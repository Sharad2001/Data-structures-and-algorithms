class Solution:
    def duplicates(self, arr, n):
        b = []
        a = []
        for i in range(n):
            a.append(0)
        for i in arr:
            a[i] += 1
        for i in range(n):
            if a[i] > 1:
                b.append(i)
        if len(b) != 0:
            return b
        else:
            return [-1]

if(__name__=='__main__'):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    res = Solution().duplicates(arr, n)
    for i in res:
        print(i,end=" ")
    print()