"""
853. Car Fleet  [Medium]

Approach:
  - Process cars from closest to the target to farthest.
  - Compute each car's time to reach the target.
  - A car that would arrive no later than the fleet ahead catches up and merges;
    otherwise it forms a new fleet. The stack holds one time per fleet.

Complexity: O(n log n) time, O(n) space
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Closest-to-target first
        cars = sorted(zip(position, speed), reverse=True)
        stack = []  # arrival time of each fleet

        for pos, spe in cars:
            time = (target - pos) / spe

            # Reaches the target before (or with) the fleet ahead: joins it
            if stack and time <= stack[-1]:
                continue

            stack.append(time)

        return len(stack)
