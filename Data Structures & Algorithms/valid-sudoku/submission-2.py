class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Valid Sudoku board: 
            Each row must contain the digits 1-9 without duplicates.
            Each column must contain the digits 1-9 without duplicates.
            Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

        Time: <= O(n^2)
        Space: <= O(n^2)
        """

        # row
        for i in range(len(board)):
            row = set()
            for j in range(len(board[0])):
                if board[i][j] in row:
                    return False
                elif board[i][j] == ".":
                    continue
                row.add(board[i][j])

        # col
        for j in range(len(board[0])):
            col = set()
            for i in range(len(board)):
                if board[i][j] in col:
                    return False
                elif board[i][j] == ".":
                    continue
                col.add(board[i][j])

        # box
        for square in range(9):
            seen = set()

            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in seen:
                        return False
                    elif board[row][col] == ".":
                        continue
                    else:
                        seen.add(board[row][col])

        return True


        