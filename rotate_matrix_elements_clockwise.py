class Solution:
    def rotateMatrix(self, M, N, Mat):
        rows = 0
        cols = 0
        halfR = M // 2
        halfC = N // 2
        while rows < halfR and cols < halfC:
            prev01 = Mat[rows + 1][cols]
            prev02 = Mat[M - rows - 2][N - cols - 1]

            temp = M - rows - 1
            for i in range(cols, N - cols):
                Mat[rows][i], prev01 = prev01, Mat[rows][i]
                Mat[temp][N - i - 1], prev02 = prev02, Mat[temp][N - i - 1]

            temp = N - cols - 1
            for i in range(rows + 1, M - rows - 1):
                Mat[i][temp], prev01 = prev01, Mat[i][temp]
                Mat[M - i - 1][cols], prev02 = prev02, Mat[M - i - 1][cols]

            rows += 1
            cols += 1
        return Mat

import math

if __name__ == '__main__':
    N, M = map(int, input().strip().split(" "))
    A = []
    for i in range(N):
        B = list(map(int, input().strip().split(" ")))
        A.append(B)
    ob = Solution()
    ans = ob.rotateMatrix(N, M, A)
    for i in range(N):
        for j in range(M):
            print(ans[i][j], end=" ")
        print()