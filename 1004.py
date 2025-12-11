'''
Use sliding window technique to find the longest subarray with at most k zeros
Maintain a count of zeros in the current window
Expand the window by moving the right pointer and include elements
If the count of zeros exceeds k, shrink the window by moving the left pointer until the count of zeros is at most k
Update the maximum length of the subarray found so far
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        left, right, out, curr = 0, 0, 0, 0
        buffer = k

        while right < n:
            while buffer > 0 and right < n:
                if nums[right] == 0:
                    buffer -= 1

                curr += 1
                right += 1
                out = max(curr, out)
            
            while right < n and nums[right] == 1:
                curr+= 1
                out = max(out, curr)
                right += 1

            while buffer == 0 and right < n:
                if nums[left] == 0:
                    buffer += 1
                curr -= 1
                left += 1
            
        return out