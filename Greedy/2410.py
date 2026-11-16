"""
2410. Maximum Matching of Players and Trainers  [Medium]

Approach (sort + two pointers):
  - Sort both lists.
  - Walk through trainers in ascending capacity; match the weakest unmatched
    player whenever the trainer can handle them.

Complexity: O(n log n + m log m) time, O(n + m) space
"""

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)

        left = 0   # next unmatched player
        right = 0  # current trainer

        out = 0  # matches

        n = len(players)
        m = len(trainers)

        while left < n and right < m:
            if players[left] <= trainers[right]:
                out += 1
                left += 1  # player matched
            right += 1     # trainer used or too weak: move on

        return out
