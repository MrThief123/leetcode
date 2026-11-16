"""
2243. Calculate Digit Sum of a String  [Easy]

Approach (simulation):
  - Split s into consecutive groups of size k (the last group may be shorter).
  - Replace each group with the sum of its digits and concatenate the results.
  - Repeat until the string length is <= k.

Complexity: O(n) per round, with the length shrinking each round; O(n) space
"""

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # Already short enough: nothing to do
        if len(s) <= k:
            return s

        while len(s) > k:
            nex = ""  # string built from this round's group sums

            i = 0  # start of the current group

            while i < len(s):
                temp = 0  # digit sum of the current group
                for _ in range(k):
                    if i >= len(s):
                        break  # last group may have fewer than k digits
                    else:
                        temp += int(s[i])
                        i += 1
                nex += str(temp)

            s = nex  # next round operates on the condensed string

        return s
