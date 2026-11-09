'''
2. Add Two Numbers
Simulate the addition of two numbers represented as linked lists, digit by digit, handling carry-over
Keep track of the carry from each addition and create new nodes for the resulting linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
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