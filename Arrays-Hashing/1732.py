"""
1732. Find the Highest Altitude  [Easy]

Approach (prefix sum):
  - altitude[i+1] = altitude[i] + gain[i], starting at altitude 0.
  - Answer is the maximum altitude reached.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = [0 for i in range(len(gain)+1)]  # prefix_sum[0] = start altitude

        for i in range(len(gain)):
            prefix_sum[i+1] = prefix_sum[i] + gain[i]

        return max(prefix_sum)
