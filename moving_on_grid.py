class Solution:
    def movOnGrid(self, r, c):
        r = (r-1) % 7
        c = (c-1) % 4
        return ["JON", "ARYA"][r==c]

if __name__ == '__main__':
    r,c =map(int,input().strip().split())
    ob = Solution();
    print(ob.movOnGrid(r,c))
