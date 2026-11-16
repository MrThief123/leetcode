"""
1657. Determine if Two Strings Are Close  [Medium]

Approach:
  - Operations allow any reordering and swapping of letter identities, so:
      1. Both words must use the same set of characters.
      2. The multiset of letter frequencies must match.
  - Build "frequency of frequencies" for each word and compare.

Complexity: O(n) time, O(1) space (alphabet is bounded)
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        from collections import defaultdict

        # Rule 1: same characters
        if set(word1) != set(word2):
            return False

        count1 = Counter(word1)  # char -> frequency
        count2 = Counter(word2)

        # frequency -> how many characters have that frequency
        count1_hash = defaultdict(int)
        count2_hash = defaultdict(int)

        for value in count1.values():
            count1_hash[value] += 1
        for value in count2.values():
            count2_hash[value] += 1

        # Rule 2: same set of frequencies...
        if set(count1_hash) != set(count2_hash):
            return False

        # ...and each frequency is shared by the same number of characters
        for key in count1_hash.keys():
            if count1_hash[key] != count2_hash[key]:
                return False
        return True
