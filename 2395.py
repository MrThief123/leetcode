class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = {}

        for i in range(len(nums) - 1):
            j = i + 1

            total = nums[i] + nums[j]

            if total in sums:
                return True
            else:
                sums[total] = True
        return False