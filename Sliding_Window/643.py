"""
643. Maximum Average Subarray I  [Easy]

Approach (fixed-size sliding window):
  - Keep a running sum of the last k elements.
  - Add the new element, record the average, then drop the oldest element.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        left = 0       # oldest element in the window
        right = k-1    # newest element in the window

        # Sum of the first k-1 elements; the loop adds the k-th
        curr_sum = sum(nums[:k-1])

        out = float('-inf')

        while right < n:
            curr_sum += nums[right]  # window now has k elements

            out = max(out, curr_sum/k)

            curr_sum -= nums[left]   # slide: drop the oldest

            left += 1
            right += 1

        return out
