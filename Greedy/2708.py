"""
2708. Maximum Strength of a Group  [Medium]

Approach (case analysis):
  - Multiply all positives (they only help).
  - Negatives help in pairs, so use an even count: if odd, drop the negative
    closest to zero (max of the negatives).
  - Edge cases: all zeros -> 0; a lone negative with no positives -> 0 if a zero
    exists, otherwise that negative itself.

Complexity: O(n log n) time, O(n) space
"""

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort()

        positives = [x for x in nums if x > 0]
        negatives = [x for x in nums if x < 0]
        zeros = nums.count(0)

        # Case 0: all zeros
        if not positives and not negatives:
            return 0

        # Case 1: no positives and only one negative
        # Choices: that negative alone, or 0 (if exists) → pick max
        if not positives and len(negatives) == 1:
            return 0 if zeros > 0 else negatives[0]

        product = 1

        # Multiply all positives
        for x in positives:
            product *= x

        # If odd number of negatives, drop the one with smallest abs (closest to zero)
        if len(negatives) % 2 == 1:
            negatives.remove(max(negatives))  # max() is the negative closest to zero

        # Multiply remaining negatives
        for x in negatives:
            product *= x

        return product
