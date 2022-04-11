class Solution:
    def numberOfCells(self, n, m, r, c, u, d, mat):
        if mat[r][c] != ".":
            return 0
        visited = {(r, c)}
        coord = [(r, c, u, d)]

        def check(row, col):
            if row >= 0 and row < n and col >= 0 and col < m and \
                    (row, col) not in visited and mat[row][col] == ".":
                visited.add((row, col))
                return True
            return False

        while coord:
            coord2 = []
            while coord:
                i, j, up, down = coord.pop()
                if check(i, j - 1):
                    coord.append((i, j - 1, up, down))
                if check(i, j + 1):
                    coord.append((i, j + 1, up, down))
                if up > 0 and check(i - 1, j):
                    coord2.append((i - 1, j, up - 1, down))
                if down > 0 and check(i + 1, j):
                    coord2.append((i + 1, j, up, down - 1))
            coord = coord2
        return len(visited)

if __name__ == '__main__':
    t = int(int(input()))

    for tcs in range(t):

        n, m, r, c, u, d = [int(x) for x in input().split()]

        mat = []

        for i in range(n):
            matele = [x for x in input()]
            mat.append(matele)
        obj = Solution()
        print(obj.numberOfCells(n, m, r, c, u, d, mat))