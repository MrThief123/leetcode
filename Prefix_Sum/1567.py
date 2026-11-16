"""
1567. Maximum Length of Subarray With Positive Product  [Medium]

Approach:
  - Zeros break the array into independent segments.
  - In each segment, count positives and negatives.
      * Even number of negatives -> the whole segment has a positive product.
      * Odd number -> drop everything up to and including the first negative,
        or everything from the last negative onward; keep the longer remainder.

NOTE: `queue, temp = []` raises ValueError (it should be `queue, temp = [], []`),
      so this does not run as written. Left unchanged.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        out = 0
        queue, temp = []  # BUG: unpacking an empty list (see NOTE)

        # Split into zero-free segments
        for num in nums:
            if num != 0:
                temp.append(num)
            else:
                if temp:
                    queue.append(temp)
                temp = []

        # The last segment isn't closed by a zero
        if nums[-1] != 0:
            queue.append(temp)

        for sub in queue:
            pos, neg = 0, 0

            for i in sub:
                if i > 0:
                    pos += 1
                else:
                    neg += 1

            if neg % 2 == 0:
                out = max(out, pos + neg)
            else:
                # Remove the prefix through the first negative
                i = 0
                while sub[i] > 0:
                    i += 1
                out = max(out, pos+neg-i-1)

                # Remove the suffix from the last negative
                i = pos + neg - 1
                while sub[i] > 0:
                    i -= 1
                out = max(out, i)

        return out
