"""
1838. Frequency of the Most Frequent Element  [Medium]

Approach (sort + sliding window):
  - After sorting, the best target for a window is its largest element (nums[right]).
  - Cost to raise every window element to nums[right] = nums[right] * length - window_sum.
  - If that cost exceeds k, shrink from the left.

Complexity: O(n log n) time, O(1) extra space
"""

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        # total = sum of the current window
        left, right, out, total = 0, 0, 0, 0

        # sliding window
        while right < n:
            total += nums[right]
            length = right - left + 1

            # If every element in the window is made equal to nums[right], e.g.
            # 5, 5, 5, 5, 5 from 1, 2, 3, 4, 5
            # the increments needed are (5-1)+(5-2)+(5-3)+(5-4)+(5-5) = 10,
            # which equals nums[right] * length - total.
            # If that needs more than k, shrink the window from the left
            # (below: nums[right]*length > total + k).
            while nums[right] * length > total + k:
                total -= nums[left]
                left += 1
                length = right - left + 1

            out = max(out, length)
            right += 1

        return out
