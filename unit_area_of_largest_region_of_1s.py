class Solution:

	def findMaxArea(self, grid):
	    n, m = len(grid), len(grid[0])
	    moves = [[-1, 0], [1, 0], [0,1],[0, -1], [1,1],
	    [-1, -1], [1, -1], [-1, 1]]
	    def dfs(x, y):
	        grid[x][y] = -1
	        ans = 1
	        for i, j in moves:
	            nx = x+i
	            ny = y+j
	            if nx >= 0 and nx < n and ny >= 0 and ny<m and grid[nx][ny]==1:
	                ans += dfs(nx, ny)
            return ans
        maxarea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxarea = max(maxarea, dfs(i, j))
        return maxarea


if __name__ == '__main__':
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        a = list(map(int, input().split()))
        grid.append(a)
    obj = Solution()
    ans = obj.findMaxArea(grid)
    print(ans)