'''
853. Car Fleet
Sort cars by starting position and calculate the time each car takes to reach the target.
Use a stack to track fleets: if a car takes less or equal time than the fleet ahead, it joins that fleet.
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spe in cars:
            time = (target - pos) / spe

            if stack and time <= stack[-1]:
                continue

            stack.append(time)

        return len(stack)
