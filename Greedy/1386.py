'''
1386. Cinema Seat Allocation
Use bitmasking to represent reserved seats in each row
Check for available blocks of 4 consecutive seats using bitwise operations
Count the maximum number of 4-seat families that can be seated
'''

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        from collections import defaultdict
        
        graph = defaultdict(int)
        out = 0

        for row, seat in reservedSeats:
            graph[row] |= 1 << (seat - 1) # set the s - 1 bit to 1

        LEFT = int('00000011110', 2) 
        MIDDLE = int('00001111000', 2)
        RIGHT = int('00111100000', 2)

        for mask in graph.values():
            can_left = (mask & LEFT) == 0
            can_middle = (mask & MIDDLE) == 0
            can_right = (mask & RIGHT) == 0

            # Case can fit
            #   00000011110 &
            #   00010000000 
            # = 00000000000

            # Case NOT fit
            #   00000011110 &
            #   00010000100 
            # = 00000000100

            if can_left and can_right: 
                out += 2 
            elif can_left or can_middle or can_right: 
                out += 1 

        out += 2 * (n - len(graph)) 
        
        return out