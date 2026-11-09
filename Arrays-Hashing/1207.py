'''
Check if the number of occurrences of each value in the array is unique
Use a hash map to count occurrences of each number
Convert the counts to a set to check for uniqueness
Return true if the size of the set equals the size of the hash map, otherwise false
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter

        counts = Counter(arr)

        return len(set(counts.values())) == len(counts.keys())