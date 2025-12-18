'''
Remove the middle node from a singly linked list using the two-pointer technique
Use a slow pointer to find the middle node and a fast pointer to reach the end of the list
Maintain a previous pointer to the node before the slow pointer to facilitate removal
If the list has only one node, return None
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode
        slow = head 
        fast = head

        if not head.next:
            return head.next

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        prev.next = slow.next
        

        return head