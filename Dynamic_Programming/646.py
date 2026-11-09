'''
646. Maximum Length of Pair Chain
Sort pairs by their ending values. Use a greedy approach to build the longest chain.
Iterate through the sorted pairs and select pairs that start after the end of the last selected pair
'''

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort by ending value
        pairs.sort(key=lambda x: x[1])

        best_end = -1001
        out = 0

        for a, b in pairs:
            if a > best_end:
                out += 1
                best_end = b

        return out