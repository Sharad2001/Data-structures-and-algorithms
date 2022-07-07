class Solution:
    def spirallyTraverse(self, matrix, r, c):
        left = 0
        right = c - 1
        top = 0
        bottom = r - 1
        direction = 0
        ans = []
        while (top <= bottom and left <= right):
            if direction == 0:
                for i in range(left, right + 1):
                    ans.append(matrix[top][i])
                top += 1
            elif direction == 1:
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            else:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
            direction = (direction + 1) % 4
        return ans

if __name__ == '__main__':
    r, c = map(int, input().strip().split())
    values = list(map(int, input().strip().split()))
    k = 0
    matrix = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(values[k])
            k += 1
        matrix.append(row)
    obj = Solution()
    ans = obj.spirallyTraverse(matrix, r, c)
    for i in ans:
        print(i, end=" ")
    print()