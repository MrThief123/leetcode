'''
1838. Frequency of the Most Frequent Element
Use a sliding window approach on the sorted array to find the longest subarray
that can be made uniform with at most k increments.
'''

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        left, right, out, total = 0, 0, 0, 0
     
        # sliding window
        while right < n:
            total += nums[right]
            length = right - left + 1

            # if all elements in window made equal to nums[right] ie 
            # 5, 5, 5, 5, 5 from 1, 2, 3, 4, 5
            # total = 15     total needed is (5-1) + (5-2) + (5-3) + (5-4) + (5-5) = 4 + 3 + 2 + 1 + 0 = 10
            # which is the same as
            # total needed = nums[right] * length - total
            # if total needed > current total + k, shrink window from left
            while nums[right] * length > total + k:
                total -= nums[left]
                left += 1
                length = right - left + 1

            out = max(out, length)
            right += 1
        
        return out