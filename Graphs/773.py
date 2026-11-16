"""
773. Sliding Puzzle  [Hard]

Approach (BFS over board states):
  - Flatten the 2x3 board to a 6-element list; the goal is (1, 2, 3, 4, 5, 0).
  - Each state is (board, index of the empty 0, moves so far).
  - Slide the 0 up/down/left/right, skipping states already seen.
  - BFS guarantees the first time we reach the goal uses the fewest moves.

Complexity: O(S) time and space, S = reachable states (at most 6! = 720)
"""

from collections import deque

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        board = board[0] + board[1]  # flatten: index = row * 3 + col
        sol = (1, 2, 3, 4, 5, 0)     # goal state

        queue = deque([(board, board.index(0), 0)])
        seen = set()
        seen.add(tuple(board))  # lists aren't hashable, so store tuples

        while queue:
            board, pos, step = queue.popleft()

            if tuple(board) == sol:
                return step

            # up (move 0 one row up)
            if pos - 3 >= 0:
                temp = board.copy()
                temp[pos], temp[pos - 3] = temp[pos - 3], temp[pos]
                if tuple(temp) not in seen:
                    queue.append((temp, pos - 3, step + 1))
                    seen.add(tuple(temp))

            # down
            if pos + 3 <= 5:
                temp = board.copy()
                temp[pos], temp[pos + 3] = temp[pos + 3], temp[pos]
                if tuple(temp) not in seen:
                    queue.append((temp, pos + 3, step + 1))
                    seen.add(tuple(temp))

            # left (not allowed from the first column)
            if pos % 3 != 0:
                temp = board.copy()
                temp[pos], temp[pos - 1] = temp[pos - 1], temp[pos]
                if tuple(temp) not in seen:
                    queue.append((temp, pos - 1, step + 1))
                    seen.add(tuple(temp))

            # right (not allowed from the last column)
            if pos % 3 != 2:
                temp = board.copy()
                temp[pos], temp[pos + 1] = temp[pos + 1], temp[pos]
                if tuple(temp) not in seen:
                    queue.append((temp, pos + 1, step + 1))
                    seen.add(tuple(temp))

        return -1  # goal unreachable
