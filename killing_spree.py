class Solution:
    def killinSpree (self, n):
        low = 1
        high = 1000000
        count = 0
        while (low<=high):
            mid = low+(high-low)//2
            val = mid*(mid+1)*(2*mid+1)//6
            if val <= n:
                ans = mid
                low = mid+1
            else:
                high = mid -1
        return ans

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ans = ob.killinSpree(N);
        print(ans)