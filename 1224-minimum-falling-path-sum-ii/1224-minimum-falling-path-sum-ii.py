class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for i in range(n - 2, -1, -1):
            min1 = min2 = float('inf')
            idx1 = -1
            for j in range(n):
                val = grid[i+1][j]
                if val < min1:
                    min2 = min1
                    min1 = val
                    idx1 = j
                elif val < min2:
                    min2 = val

            for j in range(n):
                if j == idx1:
                    grid[i][j] += min2
                else:
                    grid[i][j] += min1

        return min(grid[0])
