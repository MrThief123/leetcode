class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        out = ""
        
        for word in words:
            word_sum = 0
            for i in word:
                idx = ord(i) - ord("a")
                word_sum += weights[idx]

            idx = 26-word_sum%26+ord("a")-1
            out += chr(idx)

        return out