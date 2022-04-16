import math
class Solution:
    def rec_ww(self, nums, N, k, index, mem):
        if index == N-1:
            return 0
        if mem[index] != -1:
            return mem[index]
        _sum = 0
        _cost = math.inf
        for i in range(index, N):
            _sum += nums[i]
            if (_sum + i - index) <= k:
                if i == N-1:
                    _cost = 0
                    break
                spaces = k - (_sum  + i - index)
                _cost = min(_cost, spaces**2 + self.rec_ww(nums, N, k, i+1, mem))
            else:
                break
        mem[index] = _cost
        return mem[index]
    def solveWordWrap(self, nums, k):
        #Code here
        N = len(nums)
        mem = [-1] * N
        return self.rec_ww(nums, N, k, 0, mem)

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    obj = Solution()
    ans = obj.solveWordWrap(nums, k)
    print(ans)