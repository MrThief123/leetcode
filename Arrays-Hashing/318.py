"""
318. Maximum Product of Word Lengths  [Medium]

Approach:
  - Only the set of letters in a word matters, so keep the longest word per set.
  - Compare every pair of sets; if they share no letters, consider the product of lengths.

Complexity: O(n * L + u^2 * 26) time (u = distinct letter sets), O(u) space
"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mydict = {}  # frozenset of letters -> longest word length with that set

        # Store the maximum length of words for each unique set of characters
        for word in words:
            key = frozenset(word)
            mydict[key] = max(mydict.get(key, 0), len(word))

        keys = list(mydict.keys())
        n = len(keys)
        out = 0

        # Check pairs of sets; those with no letters in common are candidates
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not keys[i].intersection(keys[j]):
                    out = max(out, mydict[keys[i]] * mydict[keys[j]])

        return out
