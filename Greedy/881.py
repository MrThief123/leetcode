"""
881. Boats to Save People  [Medium]

Approach (sort + two pointers):
  - Every boat carries the heaviest remaining person.
  - If the lightest remaining person fits with them, take both; otherwise the
    heavy person goes alone.

Complexity: O(n log n) time, O(n) space
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        left = 0                    # lightest unboarded person
        right = len(people) - 1     # heaviest unboarded person

        out = 0    # boats used
        saved = 0  # people rescued

        while saved < len(people):
            if people[left] + people[right] <= limit:
                # Pair them up
                out += 1
                left += 1
                right -= 1
                saved += 2
            else:
                # Heaviest rides alone
                out += 1
                right -= 1
                saved += 1

        return out
