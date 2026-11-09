'''
2708. Maximum Strength of a Group
Use sorting and careful case analysis to determine which numbers to include in the product for maximum strength.
'''

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort()
        
        positives = [x for x in nums if x > 0]
        negatives = [x for x in nums if x < 0]
        zeros = nums.count(0)
        
        # Case 0: all zeros
        if not positives and not negatives:
            return 0
        
        # Case 1: no positives and only one negative
        # Choices: that negative alone, or 0 (if exists) → pick max
        if not positives and len(negatives) == 1:
            return 0 if zeros > 0 else negatives[0]
        
        product = 1
        
        # Multiply all positives
        for x in positives:
            product *= x
        
        # If odd number of negatives, drop the one with smallest abs (closest to zero)
        if len(negatives) % 2 == 1:
            negatives.remove(max(negatives))  # max() is the negative closest to zero
        
        # Multiply remaining negatives
        for x in negatives:
            product *= x
        
        return product