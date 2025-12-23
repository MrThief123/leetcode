'''
Find the number of days until a warmer temperature for each day in the list
Use a stack to keep track of indices of days with unresolved warmer temperatures
Iterate through the list of temperatures
For each temperature, pop from the stack while the current temperature is higher than the temperature at the index stored at the top of the stack
Update the output list with the difference in indices for each popped index
Push the current index onto the stack
Return the output list
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                out[index] = i - index

            stack.append(i)

        return out