'''
Using a two-pointer approach to minimize the number of rescue boats needed.
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        left = 0
        right = len(people) - 1

        out = 0
        saved = 0

        while saved < len(people):
            if people[left] + people[right] <= limit:
                out += 1
                left += 1
                right -= 1
                saved += 2
            else:
                out += 1
                right -= 1
                saved += 1

        return out