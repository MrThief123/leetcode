"""
1550. Three Consecutive Odds  [Easy]

Approach:
  - Slide a window of size 3; return True if all three values are odd.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)

        # i is the start of each window of three
        for i in range(n-2):
            if arr[i]%2 == 1:
                if arr[i+1]%2 == 1 and arr[i+2]%2 == 1:
                    return True
        return False
