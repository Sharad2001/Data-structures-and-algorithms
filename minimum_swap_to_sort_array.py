class Solution:

    def minSwaps(self, nums):
        n = len(nums)
        count = 0
        temp = nums.copy()
        h = {}
        temp.sort()
        for i in range(n):
            h[nums[i]] = i
        init = 0
        for i in range(n):
            if nums[i] != temp[i]:
                count += 1
                init = nums[i]

                nums[i], nums[h[temp[i]]] = nums[h[temp[i]]], nums[i]

                h[init] = h[temp[i]]
        return count

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    obj = Solution()
    ans = obj.minSwaps(nums)
    print(ans)