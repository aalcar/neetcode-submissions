class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # just abuse sets
        # we can check for dups with a set
        # we can have 9 sets for the rows
        # -- 9 sets for the cols
        # -- 9 sets for the sub-boxes
        # we'll use a double for loop to iterate over the entire board
        # and use the indices of both to determine which set to put an element in
        # we'll return false if any of those sets detect a duplicate
        # rows and cols are intuitive
        # sub-boxes:
        # 0: 0 <= i <= 2 and 0 <= j <= 2
        # 1: 0 <= i <= 2 and 3 <= j <= 5
        # 2: 0 <= i <= 2 and 6 <= j <= 8
        # 3: 3 <= i <= 5 and 0 <= j <= 2
        # 4: 3 <= i <= 5 and 3 <= j <= 5
        # 5: 3 <= i <= 5 and 6 <= j <= 8
        # 6: 6 <= i <= 8 and 0 <= j <= 2
        # 7: 6 <= i <= 8 and 3 <= j <= 5
        # 8: 6 <= i <= 8 and 6 <= j <= 8
        # gonna have an array of sets for the 9 sub-boxes
        # [(), (), (),
        #  (), (), (),
        #  (), (), ()]

        # integer division
        # do sub-boxes in 3x3 matrix, not sure about rows and cols
        # subboxes[i // 3][j // 3]
        # makes more sense for the others to be in a 1d array
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        subBoxSets = [[set() for _ in range(3)] for _ in range(3)]

        defaultChar = "."

        for i in range(9):
            for j in range(9):
                elem = board[i][j]

                if elem == defaultChar:
                    continue

                if elem in rowSets[i] or \
                elem in colSets[j] or \
                elem in subBoxSets[i // 3][j // 3]:
                    return False
                
                else:
                    rowSets[i].add(elem)
                    colSets[j].add(elem)
                    subBoxSets[i // 3][j // 3].add(elem)

        return True