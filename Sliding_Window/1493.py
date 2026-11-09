'''
Use sliding window technique to find the longest subarray of 1s after deleting one element
Maintain a count of the number of zeros in the current window
Expand the window by moving the right pointer and include elements
If the count of zeros exceeds 1, shrink the window by moving the left pointer until the count of zeros is at most 1
Update the maximum length of the subarray found so far  
'''

'''
Expand window right while window is valid 
Retract window left until window is valid again
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        left = 0
        out = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            out = max(out, right - left)

        return out
        


'''
Use sliding window technique to find the longest subarray of 1s after deleting one element
Maintain a count of the current length of 1s in the window
Expand the window by moving the right pointer and include elements
If a 0 is encountered, use the buffer to allow one deletion and continue
If another 0 is encountered, shrink the window by moving the left pointer until the buffer is restored
Update the maximum length of the subarray found so far
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        flip = False
        left, right, out = 0, 0, 0

        curr = -1

        buffer = 1

        while right < n:

            while buffer == 1 and right < n:
                if nums[right] == 0:
                    buffer = 0
                curr += 1
                right += 1
                out = max(curr, out)

            while buffer == 0 and right < n:
                if nums[right] == 1:
                    curr += 1
                    out = max(curr, out)
                    right += 1
                else:
                    break

            while buffer == 0:
                if nums[left] == 0:
                    buffer = 1
                curr -= 1
                left += 1
    
        return out

        