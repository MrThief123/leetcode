"""
2. Add Two Numbers  [Medium]

Approach (digit-by-digit simulation):
  - Digits are stored in reverse order, so we can add from the head directly.
  - Keep a carry; each step produces total % 10 and carries total // 10.
  - Continue while either list or a carry remains.

Complexity: O(max(n, m)) time, O(max(n, m)) space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()  # builder pointer; `out` keeps the head
        out = dummy

        total, carry = 0, 0

        # Simulate addition with carry
        while l1 or l2 or carry:
            total = carry

            # Add values from both lists if available
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            # Calculate new digit and carry
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next

        return out.next
