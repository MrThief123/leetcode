'''
Merge two sorted linked lists into one sorted linked list
Use a dummy node to simplify edge cases
Iterate through both lists, comparing the current nodes and appending the smaller one to the merged list
Once one list is exhausted, append the remaining nodes from the other list
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        # Use `and` instead of `or` and check both lists are not None
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining nodes from the non-empty list
        current.next = list1 if list1 else list2

        return dummy.next