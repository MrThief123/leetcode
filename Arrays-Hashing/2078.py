'''
2078. Two Furthest Houses With Different Colors
Iterate through the list of house colors
Track the positions of the first and last occurrence of different colors
Calculate the maximum distance based on these positions
Return the maximum distance found
'''

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        p, res = inf, 0
        for i, c in enumerate(colors):
            if (c != colors[0]):
                res = i
                p = min(p, i)
            else:
                res = max(res, i - p)
        return res