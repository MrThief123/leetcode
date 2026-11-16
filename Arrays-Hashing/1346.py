"""
1346. Check If N and Its Double Exist  [Easy]

Approach (hash lookup while scanning):
  - For each i, check whether 2*i or i/2 (only if i is even) was already seen.
  - Checking both directions covers either element appearing first.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mydict = {}  # values seen so far

        for i in arr:
            # i is half of a seen value, or double of a seen value
            if 2*i in mydict or (i%2 == 0 and i//2 in mydict):
                return True
            mydict[i] = True
        return False
