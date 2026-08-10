class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtrack in cardinal directions
        # start at every pos
        # stop if we hit the length of the word
        # without finding it
        def backtrack(index, row, col):
            if index == len(word):
                return True

            if ((row, col) in seen or 
                row < 0 or col < 0 or 
                row == len(board) or
                col == len(board[row]) or
                word[index] != board[row][col]):
                return False
            
            seen.add((row, col))
            res = (backtrack(index + 1, row - 1, col) or 
                   backtrack(index + 1, row + 1, col) or 
                   backtrack(index + 1, row, col - 1) or 
                   backtrack(index + 1, row, col + 1))
            
            seen.remove((row, col))
            return res

        seen = set()
        for row in range(len(board)):
            for col in range(len(board[row])):
                if backtrack(0, row, col):
                    return True

        return False