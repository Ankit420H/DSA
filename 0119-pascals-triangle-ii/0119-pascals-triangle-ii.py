class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []

        for row in range(rowIndex + 1):
            new_row = [1] * (row + 1)

            for j in range(1, row):
                new_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]

            triangle.append(new_row)

        return triangle[rowIndex]