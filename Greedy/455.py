'''
455. Assign Cookies
Sort both the greed factors and cookie sizes
Use two pointers to iterate through both lists
If the current cookie can satisfy the current child, increment both pointers and count the child as satisfied
If not, move to the next larger cookie
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        left, right = 0, 0

        out = 0

        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                out += 1
                right += 1
                left += 1
            else:
                right += 1

        return out