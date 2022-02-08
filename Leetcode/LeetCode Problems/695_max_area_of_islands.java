class Solution {
    private int[][] grid;
    private boolean[][] visited;

    public int dfs(int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || visited[r][c] || grid[r][c] == 0) {
            return 0;
        }
        visited[r][c] = true;
        return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1));
    }

    public int maxAreaOfIsland(int[][] grid) {
        this.grid = grid;
        visited = new boolean[grid.length][grid[0].length];
        int ans = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                ans = Math.max(ans, dfs(r, c));
            }
        }
        return ans;
    }
}
