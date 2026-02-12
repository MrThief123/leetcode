'''
318. Maximum Product of Word Lengths
Use a dictionary to store the maximum length of words for each unique set of characters. Then,
check pairs of these sets to find the maximum product of lengths for sets that have no characters in common.
'''

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mydict = {}
        
        # store the maximum length of words for each unique set of characters
        for word in words:
            key = frozenset(word)
            mydict[key] = max(mydict.get(key, 0), len(word))

        keys = list(mydict.keys()) 
        n = len(keys)
        out = 0

        # check pairs of these sets to find the maximum product of lengths for sets that have no characters in common
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not keys[i].intersection(keys[j]):
                    out = max(out, mydict[keys[i]] * mydict[keys[j]])

        return out
        