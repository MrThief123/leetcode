"""
2958. Length of Longest Subarray With at Most K Frequency  [Medium]

Approach (sliding window + frequency map):
  - Expand right and count the new element.
  - If its count exceeds k, shrink from the left until it is back to k.
  - Track the longest valid window.

Complexity: O(n) time, O(n) space
"""


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        mydict = defaultdict(int)  # element -> count inside the window

        left, right, out = 0, 0, 0
        n = len(nums)

        # expand the right pointer of the window
        while right < n:
            mydict[nums[right]] += 1
            # if the new element's count exceeds k,
            # move the left pointer right until all counts are at most k
            while mydict[nums[right]] > k:
                mydict[nums[left]] -= 1
                left += 1
            # keep track of the maximum length of the valid window
            out = max(out, right - left + 1)
            right += 1
        return out
