"""
1658. Minimum Operations to Reduce X to Zero  [Medium]

Approach (prefix sums from both ends):
  - Removing from the ends means keeping a prefix and a suffix that sum to x.
  - Record, for each prefix sum, how many elements it used; same for suffix sums.
  - For each prefix sum p, look for a suffix sum equal to x - p that doesn't
    overlap it; the operation count is prefix length + suffix length.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix_left = {}   # prefix sum -> number of elements taken from the left
        prefix_right = {}  # suffix sum -> start index of that suffix
        n = len(nums)

        prefix_left[0] = 0
        prefix_right[0] = n+1  # empty suffix starts "past the end"

        sum_left = 0
        sum_right = 0

        out = pow(10,6)  # sentinel: larger than any answer

        for i, num in enumerate(nums):
            sum_left += num
            prefix_left[sum_left] = i+1

            sum_right += nums[n-i-1]
            prefix_right[sum_right] = n-i

        for i, left in prefix_left.items():
            diff = x - i  # what the suffix must supply

            if diff in prefix_right:

                right = prefix_right[diff]

                if left < right:
                    # Elements removed = left prefix + suffix length
                    out = min(out, left + n - right+1)
                else:
                    # Prefix and suffix overlap; larger prefixes will too
                    break

        return -1 if out == 10**6 else out
