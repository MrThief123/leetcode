"""
49. Group Anagrams  [Medium]

Approach:
  - Anagrams share the same letter-frequency vector.
  - Use that vector (as a tuple) as the hash key and group words under it.

Complexity: O(n * L) time (L = word length), O(n * L) space
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        out = defaultdict(list)  # frequency tuple -> words

        out_list = []

        # Build frequency count for each word
        for word in strs:
            temp = [0 for i in range(26)]
            # Count frequency of each character
            for char in word:
                temp[ord(char) - 97] += 1

            temp = tuple(temp)  # lists aren't hashable
            out[temp].append(word)

        for word in out.values():
            out_list.append(word)

        return out_list
