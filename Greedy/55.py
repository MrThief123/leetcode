"""
55. Jump Game  [Medium]

Approach (work backwards):
  - `goal` is the leftmost index known to reach the end.
  - Scanning right to left, if index i can jump to goal, i becomes the new goal.
  - The end is reachable iff the goal makes it back to index 0.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  # start with the last index

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i  # i can reach the goal, so it becomes the goal

        return True if goal == 0 else False
