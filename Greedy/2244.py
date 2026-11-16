"""
2244. Minimum Rounds to Complete All Tasks  [Medium]

Approach (count by difficulty):
  - Each round completes 2 or 3 tasks of one difficulty.
  - A difficulty with a single task is impossible -> -1.
  - For count c: remainder 0 -> c/3 rounds; remainder 2 -> one round of 2 plus
    (c-2)/3; remainder 1 -> two rounds of 2 plus (c-4)/3.
  - (Equivalent closed form: ceil(c / 3) rounds per difficulty.)

Complexity: O(n) time, O(n) space
"""

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        from collections import Counter

        count = Counter(tasks)  # difficulty -> number of tasks
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
            # If remainder is 1, we need two extra rounds of 2 tasks (using 4 tasks)
            else:
                out += 2
                value = max(0, value - 4)
                out += value / 3

        return int(out)
