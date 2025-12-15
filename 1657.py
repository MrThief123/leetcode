'''
+Check if two strings can be transformed into each other by swapping characters
+Use hash maps to count the frequency of each character in both strings
+Compare the sets of characters and their frequency distributions
+Return true if both conditions are met, otherwise false    
'''

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        from collections import defaultdict

        if set(word1) != set(word2):
            return False

        count1 = Counter(word1)
        count2 = Counter(word2)

        count1_hash = defaultdict(int)
        count2_hash = defaultdict(int)

        for value in count1.values():
            count1_hash[value] += 1
        for value in count2.values():
            count2_hash[value] += 1

        if set(count1_hash) != set(count2_hash):
            return False 
        
        for key in count1_hash.keys():
            if count1_hash[key] != count2_hash[key]:
                return False
        return True
        