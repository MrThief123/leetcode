'''
Use a hash map to count occurrences of each number
For each unique number, check if its complement rem (k - number) exists in the map
If the number and its complement are the same, add half of its count to the result
Otherwise, add the minimum count between the number and its complement to the result
'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter

        counts = Counter(nums)

        out = 0

        for key, value in counts.items():
            rem = k - key

            if rem == key:
                out += value//2
            elif rem in counts:
                out += min(value, counts[rem])
                counts[key] = 0
                counts[rem] = 0

        return out