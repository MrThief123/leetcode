"""
503. Next Greater Element II  [Medium]

Approach (monotonic stack, two passes):
  - Keep a stack of (value, index) whose values are decreasing.
  - When a larger value arrives, pop smaller entries; it is their next greater element.
  - Loop over the array twice to simulate the circular wrap-around.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        out = [-1 for i in range(n)]  # -1 = no greater element

        stack = []  # decreasing stack of (value, index)

        # Pass 1: resolve what we can going left to right
        for n, i in enumerate(nums):
            curr = (i, n)

            while stack and curr[0] > stack[-1][0]:
                prev = stack.pop()
                out[prev[1]] = curr[0]

            stack.append(curr)

        # Pass 2: wrap around so remaining entries can see earlier values
        for n, i in enumerate(nums):
            curr = (i, n)

            while stack and curr[0] > stack[-1][0]:
                prev = stack.pop()
                out[prev[1]] = curr[0]

            stack.append(curr)

        return out
