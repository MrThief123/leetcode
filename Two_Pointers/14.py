class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        maxLen = 200
        for word in strs:
            maxLen = min(maxLen, len(word))

        best = strs[0][:maxLen]
        for word in strs:
            if not best:
                break
            for i in range(maxLen):
                if word[i] != best[i]:
                    best = word[:i]
                    maxLen = len(best)
                    break
        return best