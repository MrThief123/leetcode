'''
Find the maximum twin sum in a linked list
Use the two-pointer technique to find the middle of the list
Push the first half of the list onto a stack
Pop elements from the stack while traversing the second half to calculate twin sums
Keep track of the maximum twin sum found
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        out = float('-inf')

        stack = []

        slow = head
        fast = head

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        while slow:
            total = stack.pop() + slow.val
            out = max(total, out)
            slow = slow.next

        return out

        