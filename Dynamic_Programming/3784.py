"""
3784. Minimum Deletion Cost to Make All Characters Equal  [Medium]

Approach:
  - To make every character equal, keep one letter and delete all others.
  - Total cost of deleting everything except letter c = total cost - cost[c].
  - Sum the cost per letter and pick the letter whose kept cost is largest.

Complexity: O(n) time, O(1) space (26 letters)
"""

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        from collections import defaultdict
        mydict = defaultdict(int)  # letter -> total deletion cost of that letter
        total = 0                  # total deletion cost of all characters

        out = float('inf')

        for i in range(len(cost)):
            total += cost[i]
            mydict[s[i]] += cost[i]

        # Keep the letter whose combined cost is largest
        for i in mydict.values():
            out = min(out, total - i)

        return out
