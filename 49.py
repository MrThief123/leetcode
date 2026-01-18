'''
49. Group Anagrams
Use a frequency count of characters to group words that are anagrams.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        out = defaultdict(list)

        out_list = []

        # Build frequency count for each word
        for word in strs:
            temp = [0 for i in range(26)]
            # Count frequency of each character
            for char in word:
                temp[ord(char) - 97] += 1

            temp = tuple(temp)
            out[temp].append(word)

        for word in out.values():
            out_list.append(word)

        return out_list
