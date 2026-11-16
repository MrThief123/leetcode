"""
3026. Maximum Good Subarray Sum  [Medium]

A "good" subarray has |first - last| == k.

Approach (prefix sum + hash map):
  - Store, for each value, the minimum prefix sum before its earliest/cheapest start.
  - At each num as the subarray's last element, a good start is num - k or num + k;
    sum = prefix_including_num - prefix_before_start.
  - Return 0 if no good subarray exists.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0  # sum of elements before the current one
        best = float('-inf')
        seen = {}  # value -> minimum prefix sum before this value

        for num in nums:
            # Check both possible matches
            if num - k in seen:
                best = max(best, prefix + num - seen[num - k])

            if num + k in seen:
                best = max(best, prefix + num - seen[num + k])

            # Store the best (minimum) prefix sum for this value
            if num not in seen:
                seen[num] = prefix
            else:
                seen[num] = min(seen[num], prefix)

            prefix += num

        return 0 if best == float('-inf') else best
