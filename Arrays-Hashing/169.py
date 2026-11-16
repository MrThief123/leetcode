"""
169. Majority Element  [Easy]

Approach (Boyer-Moore voting):
  - Keep a candidate and a counter; matching values add, others cancel.
  - The majority element survives all cancellations.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = nums[0]  # current candidate
        count = 1      # its net votes

        for i in nums[1:]:
            if i == val:
                count += 1
            else:
                if count == 0:
                    # Candidate was cancelled out: adopt the new value
                    val = i
                    count += 1
                else:
                    count -= 1

        return val
