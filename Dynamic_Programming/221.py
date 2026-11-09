'''
221. Maximal Square
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Use dp to store the size of the largest square that can be formed at each position. 
The value at each position is determined by the minimum of the three adjacent positions (right, down, diagonal) 
plus one if the current cell is '1'. 
Iterate through the matrix in reverse order to fill the dp table 
and keep track of the maximum square size found.

Assume cell i,j is the top left corner of the square, then the size of the square is determined by the minimum of:
- the square size at i+1,j (down)
- the square size at i,j+1 (right)
- the square size at i+1,j+1 (diagonal)
If the current cell is '1', then we can form a square of size min(down, right, diagonal) + 1 at cell i,j.
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        F = [[0] * (C + 1) for _ in range(R + 1)]
        res = 0
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                if matrix[r][c] == '0':
                    continue
                F[r][c] = min(F[r + 1][c], F[r][c + 1], F[r + 1][c + 1]) + 1
                res = max(res, F[r][c])

        return res**2