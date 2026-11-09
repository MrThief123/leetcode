'''
773. Sliding Puzzle
The board is a 2 x 3 array, and each cell has a number from
Use a breadth-first search (BFS) approach to explore all possible board configurations.
Start with the initial board configuration and enqueue it along with the position of the zero (empty space) 
and the number of steps taken (initially 0).
Use a set to keep track of seen configurations to avoid cycles.
For each configuration, generate new configurations by sliding the zero in the four possible directions (up, down, left, right) 
    if the move is valid.
If a new configuration matches the target configuration, return the number of steps taken plus one.
If the queue is exhausted without finding the target configuration, return -1.
'''

from collections import deque

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        board = board[0] + board[1]
        sol = (1, 2, 3, 4, 5, 0)

        queue = deque([(board, board.index(0), 0)])
        seen = set()
        seen.add(tuple(board))

        while queue:
            board, pos, step = queue.popleft()

            if tuple(board) == sol:
                return step

            # up
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

            # left
            if pos % 3 != 0:
                temp = board.copy()
                temp[pos], temp[pos - 1] = temp[pos - 1], temp[pos]
                if tuple(temp) not in seen:
                    queue.append((temp, pos - 1, step + 1))
                    seen.add(tuple(temp))

            # right
            if pos % 3 != 2:
                temp = board.copy()
                temp[pos], temp[pos + 1] = temp[pos + 1], temp[pos]
                if tuple(temp) not in seen:
                    queue.append((temp, pos + 1, step + 1))
                    seen.add(tuple(temp))

        return -1