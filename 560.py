'''
use prefix sum 
then hasp to find compliment like two sum
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        n = len(nums)

        prefix = 0

        counts = defaultdict(int)
        out = 0
        counts[0] = 1

        for i in range(n):
            prefix += nums[i]
            needed = prefix - k

            if needed in counts:
                out += counts[needed]

            counts[prefix] += 1

        return out
