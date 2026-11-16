"""
2130. Maximum Twin Sum of a Linked List  [Medium]

Approach (stack for the first half):
  - slow/fast pointers find the middle while pushing the first half onto a stack.
  - Walk the second half; popping the stack yields each node's twin (mirror) value.
  - Track the largest twin sum.

Complexity: O(n) time, O(n) space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        out = float('-inf')

        stack = []  # values of the first half

        slow = head
        fast = head

        # Find the middle, stacking the first half on the way
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # Second half: the stack top is the mirrored (twin) node
        while slow:
            total = stack.pop() + slow.val
            out = max(total, out)
            slow = slow.next

        return out
