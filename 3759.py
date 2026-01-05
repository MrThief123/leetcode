'''
3759. Count Number of K-Covered Elements
Use a frequency counter to track occurrences of each element
Sort the unique elements and iterate through them
For each unique element, check if removing its occurrences keeps the remaining elements count >= k
If so, increment the result and update the total count of remaining elements
'''

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        from collections import Counter

        n = len(nums)
        out = 0

        counts = Counter(nums)

        for key in sorted(counts.keys()):
            if n - counts[key] >= k:
                out += 1
                n -= counts[key]

        return out
