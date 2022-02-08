class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visit = set()  # using hashset as memoization - mark all visited cell to prevent recursive dfs

        # dfs function -> return area of islands by connecting cells
        def dfs(r, c):
            if(r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visit):
                # cases that the island will not exist
                return 0

            # add the cell to the hashset to mark this is visited
            visit.add((r, c))

            # running dfs for 4 direction for each cell (r,c)
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))

        # iterate through all cells of grid, run dfs and find the max.
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c))

        return maxArea
