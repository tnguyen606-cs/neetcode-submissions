class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        """
        Rules: 
        - row has unique 1-9
        - col has unique 1-9
        - 3-3 sub-box has unique 1-9

        Given a 2D array, traverse through the array, return true if valid
        col.length == 9
        row.length == 9
        board[i][j] = 9 or .
        """
        
        # check row
        for i in range(len(board)): 
            row = set()

            for j in range(len(board[i])):
                if board[i][j] in row:
                    return False
                elif board[i][j] == ".":
                    continue
                else:
                    row.add(board[i][j])

        # check col
        for j in range(len(board[0])): 
            col = set()

            for i in range(len(board)):
                if board[i][j] in col:
                    return False
                elif board[i][j] == ".":
                    continue
                else:
                    col.add(board[i][j])

        # check sub-box
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











