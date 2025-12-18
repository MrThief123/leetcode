'''
Delete the middle node of a singly linked list using the two-pointer technique
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None 
        curr = head

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev