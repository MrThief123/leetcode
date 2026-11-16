"""
1052. Grumpy Bookstore Owner  [Medium]

Approach (fixed window over the grumpy minutes):
  - Customers during non-grumpy minutes are always satisfied (the base).
  - The secret technique removes grumpiness for `minutes` consecutive minutes,
    so slide a window and find the one that recovers the most grumpy customers.
  - Answer = base + best extra.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        # Customers already happy without the technique
        base = 0
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]

        extra = 0  # grumpy customers recovered within the current window
        best = 0

        for i in range(n):
            # Add the new minute if it was grumpy
            if grumpy[i] == 1:
                extra += customers[i]

            # Remove the minute that just left the window
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    extra -= customers[i - minutes]

            best = max(best, extra)

        return base + best
