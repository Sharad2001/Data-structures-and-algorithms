class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        total = 0
        hmap = {0: -1}
        ans = 0
        for idx, ele in enumerate(arr):
            total += ele
            if total not in hmap:
                hmap[total] = idx
            if total - k in hmap:
                ans = max(ans, idx - hmap[total - k])
        return ans

n, k = map(int, input().split())
arr = list(map(int, input().strip().split()))
ob = Solution()
print(ob.lenOfLongSubarr(arr, n, k))