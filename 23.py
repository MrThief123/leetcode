'''
Merge k sorted linked lists into one sorted linked list using a min-heap
Push all node values into a min-heap
Pop values from the heap to create a new sorted linked list
'''

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        mylist = []

        for head in lists:
            while head:
                heapq.heappush(mylist, head.val)
                head = head.next
            
        start = ListNode()
       
        head = start

        while mylist: 
            val = heapq.heappop(mylist)
            
            head.next = ListNode()
            head = head.next

            head.val = val
            
        return start.next