class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        m = row
        n = col

        matrix[row][col] = m x n
        matrix[row - 1][col] < matrix[row][col] < matrix[row + 1][col]

        firstRow, lastRow = 0, len(rows) - 1

        while firstRow <= lastRow:
            midRow = firstRow + ((lastRow - firstRow) // 2) 

            if target >= matrix[midRow][0] and target < matrix[lastRow][0]:
                // found the row
                l, r = 0, len(col) - 1

                binary search

            elif target > matrix[midRow][0] and target >= matrix[lastRow][0]:
                firstRow = midRow + 1
            elif target < matrix[midRow][0]:
                lastRow = midRow - 1

        """
        rows = len(matrix)
        cols = len(matrix[0])

        firstRow, lastRow = 0, rows - 1

        while firstRow <= lastRow:
            midRow = firstRow + ((lastRow - firstRow) // 2) 
            print(f"firstRow is {matrix[firstRow][0]}. midRow is {matrix[midRow][0]}. lastRow is {matrix[lastRow][0]}")

            if target >= matrix[midRow][0] and target <= matrix[midRow][cols - 1]:
                l, r = 0, cols - 1

                while l <= r:
                    midCol = l + (r - l) // 2
                    if target == matrix[midRow][midCol]:
                        return True
                    elif target < matrix[midRow][midCol]:
                        r = midCol - 1
                    else:
                        l = midCol + 1
                return False
                
            elif target > matrix[midRow][0]:
                firstRow = midRow + 1
            elif target < matrix[midRow][0]:
                lastRow = midRow - 1
                

        return False

