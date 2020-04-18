import math
from queue import PriorityQueue
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        # dp[i][j]: minimum path sum from (0, 0) to (i, j)
        dp = [[math.inf for value in row] for row in grid]
        visited = set()
        q = PriorityQueue()
        q.put((grid[0][0], (0, 0)))
        dp[0][0] = grid[0][0]

        while not q.empty():
            current_sum, current = q.get()
            if current in visited:
                continue
            visited.add(current)

            for ni, nj in self.get_neighbors(grid, *current):
                dp[ni][nj] = min(dp[ni][nj], grid[ni][nj] + current_sum)
                q.put((dp[ni][nj], (ni, nj)))

        return dp[-1][-1]

    def get_neighbors(self, grid, i, j):
        down = (i + 1, j)
        right = (i, j + 1)
        for ni, nj in (down, right):
            if ni < len(grid) and nj < len(grid[ni]):
                yield (ni, nj)
