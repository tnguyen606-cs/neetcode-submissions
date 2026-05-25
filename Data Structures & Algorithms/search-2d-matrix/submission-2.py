class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        m = row
        n = col

        matrix[row][col] = m x n
        matrix[row - 1][col] < matrix[row][col] < matrix[row + 1][col]

        """
        rows = len(matrix)
        cols = len(matrix[0])

        firstRow, lastRow = 0, rows - 1

        while firstRow <= lastRow:
            midRow = (lastRow + firstRow) // 2
            print(f"firstRow is {matrix[firstRow][0]}. midRow is {matrix[midRow][0]}. lastRow is {matrix[lastRow][0]}")

            if target >= matrix[midRow][0] and target <= matrix[midRow][-1]:
                break;
            elif target > matrix[midRow][0]:
                firstRow = midRow + 1
            elif target < matrix[midRow][0]:
                lastRow = midRow - 1
        
        if not firstRow <= lastRow:
            return False

        row = (lastRow + firstRow) // 2
        l, r, = 0, cols - 1

        while l <= r:
            midCol = l + (r - l) // 2
            if target == matrix[row][midCol]:
                return True
            elif target < matrix[row][midCol]:
                r = midCol - 1
            else:
                l = midCol + 1

        return False

