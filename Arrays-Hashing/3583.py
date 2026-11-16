"""
3583. Count Special Triplets  [Medium]

Approach:
  - For each middle index i, we need j < i < k with nums[j] == nums[k] == 2 * nums[i].
  - Store sorted index lists per value, then binary search how many matching
    indices lie left and right of i; multiply the two counts.

Complexity: O(n log n) time, O(n) space
"""

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        from collections import defaultdict
        from bisect import bisect_left, bisect_right

        pos = defaultdict(list)  # value -> sorted list of indices
        n = len(nums)
        out = 0

        # store indices for each value
        for i, num in enumerate(nums):
            pos[num].append(i)

        for i in range(1, n - 1):
            target = nums[i] * 2
            if target not in pos:
                continue

            indices = pos[target]

            # count j < i
            left = bisect_left(indices, i)

            # count k > i
            right = len(indices) - bisect_right(indices, i)

            out += left * right

        return out % (pow(10,9) + 7)
