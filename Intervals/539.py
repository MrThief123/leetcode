"""
539. Minimum Time Difference  [Medium]

Approach:
  - Convert each "HH:MM" to minutes since midnight and sort.
  - The minimum gap is between two neighbours in sorted order, or across midnight
    (wrap-around from the last time to the first).

Complexity: O(n log n) time, O(n) space
"""

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []

        for t in timePoints:
            h, m = map(int, t.split(":"))
            minutes.append(h * 60 + m)

        minutes.sort()

        ans = 1440  # minutes in a day: an upper bound

        # Gaps between consecutive times
        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i - 1])

        # Wrap-around gap: last time of the day to first time of the next
        ans = min(ans, 1440 - minutes[-1] + minutes[0])

        return ans
