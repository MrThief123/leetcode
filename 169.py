'''
169. Majority Element
Use Boyer-Moore Voting Algorithm to find the majority element in linear time and constant space.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = nums[0]
        count = 1

        for i in nums[1:]:
            if i == val:
                count += 1
            else:
                if count == 0:
                    val = i
                    count += 1
                else:
                    count -= 1

        return val