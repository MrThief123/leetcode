'''
1221. Split a String in Balanced Strings
Iterate through the string while maintaining a balance counter
Increment the counter for 'L' and decrement for 'R'
Each time the counter returns to zero, a balanced substring is found
Count and return the number of balanced substrings
'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        out = 0
        count = 0

        for c in s:
            if c == 'L':
                count += 1
            else:
                count -= 1

            if not count:
                out += 1
                count = 0

        return out
        