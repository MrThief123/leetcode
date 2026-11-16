"""
1386. Cinema Seat Allocation  [Medium]

Approach (bitmask per row):
  - Store each row's reserved seats as a bitmask (bit seat-1 set).
  - A family of four needs one of three blocks: seats 2-5 (LEFT), 4-7 (MIDDLE),
    or 6-9 (RIGHT); each block is free if mask & block == 0.
  - Both LEFT and RIGHT free -> 2 families; else any free block -> 1 family.
  - Rows with no reservations hold 2 families each.

Complexity: O(r) time (r = reservations), O(r) space
"""

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        from collections import defaultdict

        graph = defaultdict(int)  # row -> bitmask of reserved seats
        out = 0

        for row, seat in reservedSeats:
            graph[row] |= 1 << (seat - 1) # set the s - 1 bit to 1

        # Bit masks for each block of four seats (bit 0 = seat 1)
        LEFT = int('00000011110', 2)    # seats 2-5
        MIDDLE = int('00001111000', 2)  # seats 4-7
        RIGHT = int('00111100000', 2)   # seats 6-9

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
                out += 2  # left and right blocks don't overlap
            elif can_left or can_middle or can_right:
                out += 1

        # Untouched rows fit two families each
        out += 2 * (n - len(graph))

        return out
