class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # do literally the same thing as N-Queens II
        # but whenever we place a queen,
        # append board states like a generic backtracking problem
        def backtrack(board, row, seen_cols, seen_diags, seen_antis):
            if row == n:
                res.append(board[:])
                return

            for col in range(n):
                diag = row - col
                anti_diag = row + col

                if (col in seen_cols
                or diag in seen_diags
                or anti_diag in seen_antis):
                    continue

                seen_cols.add(col)
                seen_diags.add(diag)
                seen_antis.add(anti_diag)

                board_row = ['.' for _ in range(n)]
                board_row[col] = 'Q'
                board.append("".join(board_row))

                backtrack(board, row + 1, seen_cols, seen_diags, seen_antis)

                board.pop()
                seen_cols.remove(col)
                seen_diags.remove(diag)
                seen_antis.remove(anti_diag)
        
        res = []
        backtrack([], 0, set(), set(), set())
        return res