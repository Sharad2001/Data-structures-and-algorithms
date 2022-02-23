class Solution:
    def RecursivePower(self,n,p):
        self.n = n
        self.p = p
        if p == 0:
            return 1
        if p == 1:
            return n
        else:
            a = self.RecursivePower(n, p-1)
            return n * a
if __name__ == '__main__':
    n,p = map(int,input("Enter the number and its power: ").strip().split())
    print(Solution().RecursivePower(n,p))