'''
2840.

Use hash map to count letters in odd / even postions
make sure the number in s1 and s2 is equal
'''

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        even = defaultdict(int)
        odd = defaultdict(int)

        for i in range(len(s1)):
            if i%2 == 0:
                even[s1[i]] += 1
                even[s2[i]] -= 1
            else:
                odd[s1[i]] += 1
                odd[s2[i]] -= 1

        for i in even.values():
            if i != 0:
                return False
        for i in odd.values():
            if i != 0:
                return False
        return True