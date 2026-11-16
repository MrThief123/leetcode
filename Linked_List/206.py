"""
206. Reverse Linked List  [Easy]

Approach (iterative pointer reversal):
  - Walk the list, pointing each node's `next` at the previous node.
  - `prev` ends up as the new head.

Complexity: O(n) time, O(1) space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # empty or single node: already reversed

        prev = None
        curr = head

        while curr:
            nex = curr.next   # remember the rest of the list
            curr.next = prev  # flip the pointer
            prev = curr       # advance both pointers
            curr = nex

        return prev
