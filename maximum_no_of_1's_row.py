class Solution:
    def maxOnes (self, Mat, N, M):
        ans = 0
        s = 0
        count = 0
        for i in range(N):
            s = 0
            for j in range(M):
                s += Mat[i][j]
            if s > ans:
                ans = s
                count = i
        return count

if __name__ == '__main__':
    size = input().strip().split()
    r = int(size[0])
    c = int(size[1])
    line = list(map(int,input().split()))
    matrix = [ [0 for _ in range(c)] for _ in range(r) ]
    for i in range(r):
        for j in range(c):
            matrix[i][j] = line[i*c+j]
    ob = Solution()
    print(ob.maxOnes(matrix,r,c))