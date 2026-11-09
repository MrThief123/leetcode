'''
Implement a RecentCounter class to count recent requests within a 3000 milliseconds window
Use a deque to store the timestamps of requests
When a new request comes in, add its timestamp to the deque
Remove timestamps from the front of the deque that are older than t - 3000
Return the size of the deque, which represents the number of recent requests
'''

from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        
        # Remove requests older than t - 3000
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        
        return len(self.queue)
