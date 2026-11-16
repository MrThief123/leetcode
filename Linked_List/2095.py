"""
2095. Delete the Middle Node of a Linked List  [Medium]

Approach (slow/fast pointers):
  - fast moves two steps per slow's one, so slow lands on the middle.
  - Track `prev` (node before slow) to unlink the middle.
  - A single-node list becomes empty.

Complexity: O(n) time, O(1) space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode  # placeholder; reassigned in the loop
        slow = head
        fast = head

        # One node: deleting it leaves an empty list
        if not head.next:
            return head.next

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next

        # slow is the middle: skip over it
        prev.next = slow.next

        return head
