"""
1470. Shuffle the Array  [Easy]

Approach:
  - nums is [x1,...,xn,y1,...,yn]; the target is [x1,y1,x2,y2,...,xn,yn].
  - Build the output directly: out[2*i] = nums[i], out[2*i+1] = nums[i+n].

Complexity: O(n) time, O(n) space
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = [0] * 2 * n

        for i in range(n):
            out[i*2] = nums[i]
            out[i*2+1] = nums[i+n]

        return out
