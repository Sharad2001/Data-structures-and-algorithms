class Solution:
    def countShare(self, B):

        self.B = B
        cnt = 0
        for i in range((B - 2) // 2):
            cnt += (B - 2) // 2 - i
        return cnt

if __name__ == "__main__":
    b = int(input().strip())
    obj = Solution()
    print(obj.countShare(b))