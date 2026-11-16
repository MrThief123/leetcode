"""
3683. Earliest Time to Finish Last Task  [Easy]

Approach:
  - Each task is [start, duration], so it finishes at start + duration.
  - The earliest finish time over all tasks is the minimum of those sums.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        best = float('inf')  # earliest completion time found

        for start, time in tasks:
            best = min(best, start+time)
        return best
