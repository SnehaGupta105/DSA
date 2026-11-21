
class Solution(object):
    def spiralOrder(self, matrix):
        result = []

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        while top <= bottom and left <= right:

            # 1. Left to Right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # 2. Top to Bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # 3. Right to Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # 4. Bottom to Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
