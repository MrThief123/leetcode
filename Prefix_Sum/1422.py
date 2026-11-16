"""
1422. Maximum Score After Splitting a String  [Easy]

Approach (prefix counts):
  - Score of a split = zeros on the left + ones on the right.
  - Precompute running counts of zeros and ones for each split point.
  - Right ones = total ones - ones on the left; try every split.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        # Index i = split after position i (both sides must be non-empty)
        prefix_left = [0 for i in range(n-1)]   # zeros in s[0..i]
        prefix_right = [0 for i in range(n-1)]  # ones in s[0..i]
        count = int(s[-1])                      # start the ones total with the last char

        if s[0] == '0':
            prefix_left[0] = 1
        else:
            prefix_right[0] = 1

        for i in range(1, n-1, 1):
            prefix_left[i] = prefix_left[i-1]
            prefix_right[i] = prefix_right[i-1]

            if s[i] == '0':
                prefix_left[i] += 1
            else:
                prefix_right[i] += 1

        count += prefix_right[-1]  # total ones in the whole string

        out = 0

        for i in range(len(prefix_right)):
            # zeros on left + (total ones - ones on left)
            out = max(out, prefix_left[i] + count - prefix_right[i])

        return out
