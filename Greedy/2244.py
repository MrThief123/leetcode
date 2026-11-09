'''
2244. Minimum Rounds to Complete All Tasks
Count the frequency of each task and determine the minimum rounds needed. Each round can complete either 2 or 3 tasks of the same type.
If any task appears only once, return -1 as it's impossible to complete that task.
Check the frequency of each task and calculate the minimum rounds accordingly.
'''

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        from collections import Counter

        count = Counter(tasks)
        out = 0

        for value in count.values():
            # If any task appears only once, return -1 not possible
            if value < 2:
                return -1
            
            # Calculate minimum rounds based on frequency
            if value % 3 == 0:
                out += value / 3
            # If remainder is 2, we need one extra round of 2 tasks
            elif value % 3 == 2:
                out += 1
                value = max(0, value - 2)
                out += value / 3
            # If remainder is 1, we need one extra round of 2 tasks
            else:
                out += 2
                value = max(0, value - 4)
                out += value / 3

        return int(out)