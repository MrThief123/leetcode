

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        out = []
        n = len(s)

        if n < 3:
            return out

        left = 0
        right = 0

        while right < n:
            while right + 1 < n and s[left] == s[right+1]:
                right += 1

            if right - left  >= 2:
                out.append([left, right])
            left = right + 1
            right = left

        return out

