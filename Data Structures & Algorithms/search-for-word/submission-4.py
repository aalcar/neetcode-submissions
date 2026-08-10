class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtrack in cardinal directions
        # start at every pos
        # stop if we hit the length of the word
        # without finding it
        def backtrack(partial, row, col, seen):
            if len(partial) == len(word):
                return partial == word

            if partial != word[:len(partial)]:
                return
            
            is_above, is_down, is_left, is_right = False, False, False, False
            if row > 0 and (row - 1, col) not in seen:
                seen.add((row - 1, col))
                is_above = backtrack(partial + board[row - 1][col], row - 1, col, seen)
                seen.remove((row - 1, col))

            if row < len(board) - 1 and (row + 1, col) not in seen:
                seen.add((row + 1, col))
                is_down = backtrack(partial + board[row + 1][col], row + 1, col, seen)
                seen.remove((row + 1, col))
            
            if col > 0 and (row, col - 1) not in seen:
                seen.add((row, col - 1))
                is_left = backtrack(partial + board[row][col - 1], row, col - 1, seen)
                seen.remove((row, col - 1))
        
            if col < len(board[row]) - 1 and (row, col + 1) not in seen:
                seen.add((row, col + 1))
                is_right = backtrack(partial + board[row][col + 1], row, col + 1, seen)
                seen.remove((row, col + 1))

            # print("partial: ", partial)
            # print("board[r][c]", board[row][col])
            # print("is_down: ", is_down)
            # print("is_above: ", is_above)
            # print("is_right: ", is_right)
            # print("is_left: ", is_left)
            # print(" ")

            return is_down or is_above or is_right or is_left

        for row in range(len(board)):
            for col in range(len(board[row])):
                if backtrack(board[row][col], row, col, {(row,col)}):
                    return True

        return False