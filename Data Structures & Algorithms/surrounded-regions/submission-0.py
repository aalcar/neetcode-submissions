class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # scan borders.
        # start dfs on any O's
        # mark visited
        # iterate through grid
        # -- if not in visited, replace with X

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if (min(r, c) < 0 or 
                    r == ROWS or 
                    c == COLS or 
                    (r, c) in visited or 
                    board[r][c] != "O"):
                return

            visited.add((r, c))

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"
