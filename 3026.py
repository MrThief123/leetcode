'''
3026. Maximum Subarray Sum With Exactly K Different Integers
Use prefix sums and a hashmap to track the minimum prefix sum for each integer value.
'''

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
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
