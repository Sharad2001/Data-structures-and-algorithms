class Solution:
    def isMonotonic(self, nums):
        return sorted(nums) == nums or sorted(nums, reverse=True) == nums

if __name__ == '__main__':
    nums = list(map(int, input().strip().split()))
    obj = Solution()
    ans = obj.isMonotonic(nums)
    print(ans)