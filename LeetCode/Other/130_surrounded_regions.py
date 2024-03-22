class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])

        # function to find unsurrounded "O" (check for each cell of the board)
        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"

            # run this dfs on all directions
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)

        # 1. Capture unsurrounded regions ( change all unsurrounded O -> T) (using DFS)
        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS-1])):
                    capture(r, c)

        # 2. capture surrounded regions ( change all surrounded O -> X)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions ( change back T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
