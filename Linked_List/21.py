"""
21. Merge Two Sorted Lists  [Easy]

Approach (dummy head + splice):
  - A dummy node avoids special-casing the first node.
  - Repeatedly attach the smaller head of the two lists.
  - When one list is exhausted, attach the rest of the other.

Complexity: O(n + m) time, O(1) space (nodes are reused)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy  # tail of the merged list

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
