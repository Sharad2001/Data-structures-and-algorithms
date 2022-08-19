from heapq import heapify, heappush, heappop
import math
class Solution:
    def __init__(self):
        self.small, self.large = [], []
        heapify(self.small)
        heapify(self.large)

    def balanceHeaps(self):
        # Balance the two heaps size , such that difference is not more than one.
        # code here
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heappop(self.small)
            heappush(self.large, val)
        if len(self.small) - len(self.large) > 1:
            val = -heappop(self.small)
            heappush(self.large, val)
        if len(self.large) - len(self.small) > 1:
            val = -heappop(self.large)
            heappush(self.small, val)


    def getMedian(self):
        # return the median of the data received till now.
        # code here
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2

    def insertHeaps(self, x):
        heappush(self.small, -x)
        self.balanceHeaps()


if __name__ == '__main__':
    n = int(input())
    ob = Solution()
    for i in range(n):
        x = int(input())
        ob.insertHeaps(x)
        print(math.floor(ob.getMedian()))