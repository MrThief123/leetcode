"""
2110. Number of Smooth Descent Periods of a Stock  [Medium]

Approach:
  - A smooth descent is a run where each price is exactly 1 lower than the previous.
  - A run of length L contributes L*(L+1)/2 periods (every sub-run).
  - Build runs on a stack; when the run breaks, add its contribution and restart.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # Number of periods in a run of length n: 1 + 2 + ... + n
        def helper(n):
            out = 0
            for i in range(n):
                out += 1 + i
            return out

        stack = []  # current descending run
        out = 0

        for price in prices:
            if not stack or stack[-1] - 1 == price:
                stack.append(price)  # run continues
            else:
                # Run ended: bank its periods and start a new run
                n = len(stack)
                out += helper(n)
                stack = []
                stack = [price]

        # Don't forget the final run
        if stack:
            out += helper(len(stack))
        return out
