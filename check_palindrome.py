class Solution:
    def isPalin(self, N):
        N = str(N)
        if len(N) <= 1:
            return 1
        else:
            if N[0] == N[-1]:
                return self.isPalin(N[1:-1])
            else:
                return 0

if __name__ == '__main__':

    n = int(input("Enter the number: "))
    obj = Solution()
    print(int(obj.isPalin(n)))
