'''
1304. Find N Unique Integers Sum up to Zero
To generate n unique integers that sum up to zero, we can pair positive and negative integers.
If n is odd, we include zero in the list.
'''

class Solution:
    def sumZero(self, n: int) -> List[int]:
        out = []
        if n % 2 == 0:
            for i in range(1, n//2 + 1, 1):
                out.extend([i, -i])
        else:
            for i in range(1, n//2 + 1, 1):
                out.extend([i, -i])
            out.append(0)
        return out