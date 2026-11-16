"""
2869. Minimum Operations to Collect Elements  [Easy]

Approach:
  - Removing from the end is the same as scanning the array backwards.
  - Mark each value in 1..k the first time we see it.
  - Stop once all k values are collected; the answer is the number of elements scanned.

Complexity: O(n) time, O(k) space
"""

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        used = [False for i in range(k+1)]  # used[v] = collected value v
        out = 0       # elements removed so far
        temp = k      # values still needed

        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= k and used[nums[i]] == False:
                used[nums[i]] = True
                temp -= 1
            out += 1

            if temp == 0:
                return out
