'''
79. Word Search
Use DFS to explore all possible paths in the grid.
Prune paths early if the current cell does not match the expected character in the word.
Maintain a set of visited cells to avoid cycles.
Before starting the DFS, perform a frequency check to ensure that the board 
contains enough of each character needed to form the word. This can help prune impossible cases early on.
'''

from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        n = len(word)

        # ---- pruning: frequency-based ----
        board_counter = Counter()
        for i in range(rows):
            for j in range(cols):
                board_counter[board[i][j]] += 1

        word_counter = Counter(word)
        for ch in word_counter:
            if word_counter[ch] > board_counter[ch]:
                return False   # impossible to form the word

        # ---- DFS ----
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j, pos, seen):
            if pos == n:
                return True

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < rows and 0 <= nj < cols:
                    if (ni, nj) not in seen and board[ni][nj] == word[pos]:
                        seen.add((ni, nj))
                        if dfs(ni, nj, pos + 1, seen):
                            return True
                        seen.remove((ni, nj))  # backtrack, 
                        # set postion to unvisited as we return to it from the next recursive call

            return False

        # ---- Try every starting position ----
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    seen = {(i, j)}
                    if dfs(i, j, 1, seen):
                        return True

        return False