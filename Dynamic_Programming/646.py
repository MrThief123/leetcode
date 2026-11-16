"""
646. Maximum Length of Pair Chain  [Medium]

Approach (greedy, like interval scheduling):
  - Sort pairs by end value.
  - Take a pair whenever it starts after the end of the last chosen pair; this
    leaves the most room for later pairs.

Complexity: O(n log n) time, O(1) extra space
"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort by ending value
        pairs.sort(key=lambda x: x[1])

        best_end = -1001  # below the minimum possible value (-1000)
        out = 0

        for a, b in pairs:
            if a > best_end:
                out += 1
                best_end = b  # chain now ends here

        return out
