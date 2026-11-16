"""
1004. Max Consecutive Ones III  [Medium]

Approach (sliding window with a flip budget):
  - `buffer` is how many zeros we may still flip.
  - Phase 1: expand right, spending the buffer on zeros.
  - Phase 2: while the next element is 1, extend for free.
  - Phase 3: when the budget is gone and a zero blocks us, shrink from the left
    until a zero leaves the window (refunding one flip).
  - Track the longest window.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # left/right: window bounds, out: best length, curr: current window length
        left, right, out, curr = 0, 0, 0, 0
        buffer = k  # flips remaining

        while right < n:
            # Expand while we still have flips
            while buffer > 0 and right < n:
                if nums[right] == 0:
                    buffer -= 1

                curr += 1
                right += 1
                out = max(curr, out)

            # Free extension over ones
            while right < n and nums[right] == 1:
                curr += 1
                out = max(out, curr)
                right += 1

            # Out of flips: shrink until a zero leaves the window
            while buffer == 0 and right < n:
                if nums[left] == 0:
                    buffer += 1
                curr -= 1
                left += 1

        return out
