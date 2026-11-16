"""
1423. Maximum Points You Can Obtain from Cards  [Medium]

Approach (prefix sums):
  - We take k cards total from the two ends: i from the front, k-i from the back.
  - With prefix sums, the front is prefix[i] and the back is total - prefix[n-(k-i)].
  - Try every split i = k, k-1, ..., 0 and keep the best.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        left = k     # number of cards taken from the front
        right = n    # start index of the back segment (nothing from the back yet)
        out = float('-inf')

        prefix_sum = [0 for i in range(n+1)]

        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + cardPoints[i]

        # Each step moves one card from the front to the back
        for i in range(k+1):
            total = prefix_sum[left] + prefix_sum[-1] - prefix_sum[right]
            out = max(out, total)
            left -= 1
            right -= 1

        return out
