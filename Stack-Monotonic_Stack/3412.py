"""
3412. Find Mirror Score of a String  [Medium]

A letter's mirror is its reverse-alphabet partner (a<->z, b<->y, ...).

Approach (per-letter stacks of indices):
  - Keep, for each letter, a stack of indices not yet paired.
  - At index i, if an earlier unpaired mirror letter exists, pair with the closest
    one (top of its stack) and add i - j to the score.
  - Otherwise record i for later.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def calculateScore(self, s: str) -> int:
        # Mirror of c: 'a'(97)->'z'(122), 'b'->'y', ...
        def fliper(c):
            return chr(122 - ord(c) + 97)

        from collections import defaultdict

        score = 0
        mydict = defaultdict(list)  # letter -> indices still unpaired

        for i, c in enumerate(s):
            flip = fliper(c)
            if flip in mydict and mydict[flip]:
                # Pair with the closest unpaired mirror letter
                score += i - mydict[flip].pop()
            else:
                mydict[c].append(i)

        return score
