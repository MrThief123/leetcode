'''
Find largest value
check if each value + extraCandies >= largest
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        largest = max(candies)

        out = [i + extraCandies >= largest for i in candies]

        return out