'''
15. 3Sum
Sort
for each triplet i, j, k
    lock unqiue value of i
    move j and k to find the sum of 0, use two pointer technique
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []
        nums.sort()
        n = len(nums)

        for i, a in enumerate(nums):
            # check if not same value we have already seen
            if i > 0 and a == nums[i-1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    out.append ([a, nums[left], nums [right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
        return out