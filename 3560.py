class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        out = 0

        if n > k:
            out += k * (n-k)
        if m > k:
            out += k * (m-k)
        return out
