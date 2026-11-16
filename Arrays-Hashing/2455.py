"""
2455. Average Value of Even Numbers That Are Divisible by Three  [Easy]

Approach:
  - Even and divisible by 3 means divisible by 6; sum and count those values.
  - Return the integer average, or 0 when there are none.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        temp = 0  # running sum
        c = 0     # how many qualify

        for i in nums:
            if i %3 == 0 and i%2 == 0:
                temp += i
                c += 1
        return int(temp/c) if c != 0 else 0
