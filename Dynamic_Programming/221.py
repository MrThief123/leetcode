"""
221. Maximal Square  [Medium]

Approach (DP from the bottom-right):
  - F[r][c] = side length of the largest all-1 square whose top-left corner is (r, c).
  - If the cell is '1': F = 1 + min(down, right, diagonal-down-right).
  - Track the largest side and return its area.

Complexity: O(rows * cols) time, O(rows * cols) space
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        F = [[0] * (C + 1) for _ in range(R + 1)]  # padded so r+1 / c+1 are always valid
        res = 0  # largest side length found
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                if matrix[r][c] == '0':
                    continue
                F[r][c] = min(F[r + 1][c], F[r][c + 1], F[r + 1][c + 1]) + 1
                res = max(res, F[r][c])

        return res**2  # area = side squared
