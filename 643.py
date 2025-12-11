'''
Use sliding window technique to find maximum average of subarray with length k
Maintain a running sum of the current window
Slide the window by adding the next element and removing the first element of the previous window
Update the maximum average found so far
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        left = 0
        right = k-1

        curr_sum = sum(nums[:k-1])

        out = float('-inf')

        while right < n:
            curr_sum += nums[right]

            out = max(out, curr_sum/k)

            curr_sum -= nums[left]

            left += 1
            right += 1

        return out