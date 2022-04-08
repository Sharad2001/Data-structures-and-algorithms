class Solution:
    def print_next_greater_freq(self,arr,n):
        freq = {}
        for i in range(n):
            if arr[i] in freq:
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1
        ans = [-1 for i in range(n)]
        stack = []
        stack.append(arr[n-1])
        for i in range(n-2, -1, -1):
            while (stack and freq[stack[-1]] <= freq[arr[i]]):
                stack.pop()
            if len(stack) == 0:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
            stack.append(arr[i])
        return ans

if __name__ == '__main__':
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    obj=Solution()
    ans=obj.print_next_greater_freq(arr,n)
    for i in ans:
        print(i,end=" ")
    print()