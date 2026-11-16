"""
79. Word Search  [Medium]

Approach (DFS + backtracking):
  - Pruning: if the board lacks enough of any letter in the word, fail immediately.
  - From each cell matching word[0], DFS to adjacent cells matching the next letter.
  - A `seen` set prevents reusing a cell within one path; remove from it when backtracking.

Complexity: O(rows * cols * 3^len(word)) time, O(len(word)) space
"""

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

        # (i, j) is the last matched cell, pos is the next letter index to match
        def dfs(i, j, pos, seen):
            if pos == n:
                return True  # matched every letter

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
