"""
3838. Weighted Word Mapping  [Easy]

Approach:
  - Sum the weights of each word's letters.
  - Map the sum mod 26 to a letter in reverse alphabet order (0 -> 'z', 1 -> 'y', ...).
  - Concatenate the letters for all words.

Complexity: O(total characters) time, O(w) space
"""

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        out = ""

        for word in words:
            word_sum = 0
            for i in word:
                idx = ord(i) - ord("a")  # letter -> 0..25
                word_sum += weights[idx]

            # Reverse alphabet position: remainder 0 -> 'z', 25 -> 'a'
            idx = 26-word_sum%26+ord("a")-1
            out += chr(idx)

        return out
