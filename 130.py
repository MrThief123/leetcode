'''
130. Surrounded Regions
Use DFS to mark 'O's connected to the border as safe
After marking, convert unmarked 'O's to 'X's and safe 'O's back to 'O's
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows = len(board)
        columns = len(board[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, column):
            board[row][column] = 'A'

            for dr, dc in directions:
                x = row + dr
                y = column + dc

                if 0 <= x < rows and 0 <= y < columns and board[x][y] == 'O':
                    dfs(x, y)

        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][columns - 1] == 'O':
                dfs(i, columns - 1)

        for j in range(columns):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
