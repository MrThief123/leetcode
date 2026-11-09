'''
2958. Maximum Length of a Subarray With at Most K Occurrences of Each Element
Use a sliding window approach to find the longest subarray that contains at most k occurrences of each element.
Maintain a dictionary to count the occurrences of each element in the current window.
Expand the right pointer of the window and update the counts in the dictionary.
If any element's count exceeds k, move the left pointer of the window to the right until all counts are at most k.
Keep track of the maximum length of the valid window throughout the process
'''


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        mydict = defaultdict(int)

        left, right, out = 0, 0, 0
        n = len(nums)
        
        # expand the right pointer of the window
        while right < n:
            mydict[nums[right]] += 1
             # if any element's count exceeds k, 
             # move the left pointer of the window to the right until all counts are at most k
            while mydict[nums[right]] > k:
                mydict[nums[left]] -= 1
                left += 1
            # keep track of the maximum length of the valid window throughout the process
            out = max(out, right - left + 1)
            right += 1
        return out