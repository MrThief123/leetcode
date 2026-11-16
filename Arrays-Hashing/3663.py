"""
3663. Find The Least Frequent Digit  [Easy]

Approach:
  - Count each digit.
  - Take the minimum of (frequency, digit) tuples so ties go to the smaller digit.

Complexity: O(d) time (d = digits), O(1) space
"""

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        from collections import defaultdict

        count = defaultdict(int)  # digit char -> frequency

        for i in str(n):
            count[i] += 1

        out = (float('inf'), float('inf'))  # (frequency, digit)

        for key, value in count.items():
            out = min(out, (value, int(key)))

        return out[1]
