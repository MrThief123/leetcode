"""
1493. Longest Subarray of 1's After Deleting One Element  [Medium]

Idea: find the longest window containing at most one zero; the deleted element
is that zero (or any element if there is none), so the answer is window size - 1.

Complexity: O(n) time, O(1) space
"""

# Version 1 (clean): expand right, shrink left while the window has > 1 zero
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0  # zeros inside the window
        left = 0
        out = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # Window invalid: shrink until at most one zero remains
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Window size minus the one element we must delete
            out = max(out, right - left)

        return out


# Version 2 (earlier attempt): same idea with an explicit "buffer" for the one allowed zero
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        flip = False  # unused
        left, right, out = 0, 0, 0

        curr = -1  # starts at -1 to account for the mandatory deletion

        buffer = 1  # 1 = the zero allowance is unused, 0 = used

        while right < n:

            # Expand until the allowance is spent on a zero
            while buffer == 1 and right < n:
                if nums[right] == 0:
                    buffer = 0
                curr += 1
                right += 1
                out = max(curr, out)

            # Keep extending across ones; stop at the next zero
            while buffer == 0 and right < n:
                if nums[right] == 1:
                    curr += 1
                    out = max(curr, out)
                    right += 1
                else:
                    break

            # Shrink from the left until the used zero leaves the window
            while buffer == 0:
                if nums[left] == 0:
                    buffer = 1
                curr -= 1
                left += 1

        return out
