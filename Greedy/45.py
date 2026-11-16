"""
45. Jump Game II  [Medium]

Approach (greedy BFS-by-levels):
  - `currEnd` is the farthest index reachable with the current number of jumps;
    `farthest` is the farthest reachable with one more jump.
  - On reaching currEnd, we must jump again: count it and extend currEnd to `farthest`.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currEnd = 0    # end of the range covered by the current jump count
        farthest = 0   # best reach seen so far

        # The last index needs no jump from it, so stop at n - 2
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == currEnd:
                jumps += 1           # take another jump
                currEnd = farthest

        return jumps
