
# exercise link: https://leetcode.com/problems/minimum-path-sum/

#####################################################################

#Dynamic Programming: Using O(1) space
# - Space complexity can be reduced to O(1) as grid can be reused as cost matrix
# -Notice how we iterate the two loops and the special condition we use for i=0

####################################################################

class Solution(object):
    def minPathSum(self, grid):
        M, N = len(grid), len(grid[0])
        for i in range(M):
            grid[i][0] = grid[i][0] + grid[i-1][0] if i > 0 else grid[i][0]
            for j in range(1,N):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j] if i > 0 else grid[i][j-1]+grid[i][j]
        return grid[-1][-1]