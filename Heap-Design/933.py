"""
933. Number of Recent Calls  [Easy]

Approach (queue as sliding time window):
  - Append each ping time to a deque.
  - Evict timestamps older than t - 3000 from the front.
  - The deque length is the number of requests in [t - 3000, t].

Complexity: O(1) amortised per ping, O(w) space (w = pings in the window)
"""

from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()  # timestamps, oldest first

    def ping(self, t: int) -> int:
        self.queue.append(t)

        # Remove requests older than t - 3000
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)
