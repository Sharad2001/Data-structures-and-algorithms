import math
class Solution:
    def countSetBits(self,n):
        count = 0
        m = int(math.log(n, 2))
        while (m >= 0):
            b = (n+1)//(2**m)
            count += (b // 2) * (2**m)
            if b % 2 != 0:
                count += (n+1)%(2**m)
            m -= 1
        return count

if __name__=="__main__":
    ob=Solution()
    print(ob.countSetBits(int(input())))