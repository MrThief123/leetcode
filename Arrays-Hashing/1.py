"""
1. Two Sum  [Easy]

Approach (one-pass hash map):
  - Store each number's index as we scan.
  - For every num, look up (target - num); if seen, we have the pair.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}  # value -> index where we saw it

        for i, num in enumerate(nums):
            difference = target - num  # the partner we need

            if difference in mydict:
                return [mydict[difference], i]
            else:
                mydict[num] = i
