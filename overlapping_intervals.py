class Solution:
    def overlappedInterval(self, Intervals):
        Intervals.sort()
        stack = []
        res = []
        stack.append(Intervals[0])
        for i in Intervals[1:]:
            if stack[-1][0] <= i[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], i[-1])
            else:
                stack.append(i)
        for i in range(len(stack)):
            res.append(stack[i])
        return res

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    Intervals = []
    j = 0
    for i in range(n):
        x = a[j]
        j += 1
        y = a[j]
        j += 1
        Intervals.append([x, y])
    obj = Solution()
    ans = obj.overlappedInterval(Intervals)
    for i in ans:
        for j in i:
            print(j, end=" ")
    print()