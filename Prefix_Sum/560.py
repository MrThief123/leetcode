"""
560. Subarray Sum Equals K  [Medium]

Approach (prefix sum + hash map, like Two Sum):
  - Subarray (j, i] sums to k exactly when prefix[i] - prefix[j] == k.
  - For each prefix, look up how many earlier prefixes equal (prefix - k).
  - Seed counts[0] = 1 so subarrays starting at index 0 are counted.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        n = len(nums)

        prefix = 0  # running sum

        counts = defaultdict(int)  # prefix sum -> times seen
        out = 0
        counts[0] = 1  # empty prefix

        for i in range(n):
            prefix += nums[i]
            needed = prefix - k  # earlier prefix that would make a sum of k

            if needed in counts:
                out += counts[needed]

            counts[prefix] += 1

        return out
