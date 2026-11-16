"""
739. Daily Temperatures  [Medium]

Approach (monotonic decreasing stack of indices):
  - The stack holds days still waiting for a warmer day.
  - A warmer day pops every colder day on the stack; the gap in indices is their answer.

Complexity: O(n) time, O(n) space
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # indices of days with no warmer day found yet
        out = [0 for i in range(len(temperatures))]  # 0 = never gets warmer

        for i in range(len(temperatures)):
            # Today is warmer than the waiting days on top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                out[index] = i - index

            stack.append(i)

        return out
