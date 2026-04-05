'''
657. Robot Return to Origin
Count if U == D and L == R
'''

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter

        count = Counter(moves)

        if count['U'] == count['D'] and count['L'] == count['R']:
            return True
        return False