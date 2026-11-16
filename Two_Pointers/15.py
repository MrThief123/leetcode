"""
15. 3Sum  [Medium]

Approach (sort + two pointers):
  - Sort, then fix each value a as the first element of a triplet.
  - Use two pointers on the remainder to find pairs summing to -a.
  - Skip repeated values for both a and the pointers to avoid duplicate triplets.

Complexity: O(n^2) time, O(1) extra space (ignoring output and sort)
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []
        nums.sort()
        n = len(nums)

        for i, a in enumerate(nums):
            # Skip a value we already used as the first element
            if i > 0 and a == nums[i-1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1  # too big: need a smaller value
                elif threeSum < 0:
                    left += 1   # too small: need a larger value
                else:
                    out.append ([a, nums[left], nums [right]])
                    left += 1
                    # Skip duplicates of the left value
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return out
