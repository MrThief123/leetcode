'''
287. Find the Duplicate Number
Use the "Floyd's Tortoise and Hare" algorithm to detect the cycle in the
linked list representation of the array, where the duplicate number is the entry point of the cycle.

ie
0 1 2 3 4 5
0 1 2 3 4 2

slow = 0, fast = 0
slow = 1, fast = 2
slow = 2, fast = 4

'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Detect cycle
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Step 2: Find entrance to cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

            