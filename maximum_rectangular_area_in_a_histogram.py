class Solution:
    def getMaxArea(self, arr):
        stack = [0]
        arr.append(0)
        ans = 0
        for i in range(1, len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                idx = stack.pop()
                h = arr[idx]
                w = i - stack[-1] - 1 if stack else i
                ans = max(ans, h * w)
            stack.append(i)
        return ans

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.getMaxArea(a))