"""
287. Find the Duplicate Number  [Medium]

Approach (Floyd's tortoise and hare):
  - Treat i -> nums[i] as a linked list; the duplicate value is where two
    indices point at the same node, i.e. the entry point of a cycle.
  - Phase 1: slow moves 1 step, fast moves 2, until they meet inside the cycle.
  - Phase 2: restart slow at the head; moving both 1 step, they meet at the cycle entry.

  Example:
    index: 0 1 2 3 4 5
    nums : 0 1 2 3 4 2
    slow = 0, fast = 0
    slow = 1, fast = 2
    slow = 2, fast = 4

Complexity: O(n) time, O(1) space
"""

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
