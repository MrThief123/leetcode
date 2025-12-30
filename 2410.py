'''
2410. Maximum Matching of Players With Trainers
Use a two-pointer technique to match players with trainers
Sort both the players' skill levels and trainers' capacities
Iterate through both lists, matching players to trainers when possible
Count the number of successful matches
'''

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)

        left = 0
        right = 0

        out = 0

        n = len(players)
        m = len(trainers)

        while left < n and right < m:
            if players[left] <= trainers[right]:
                out += 1
                left += 1
            right += 1

        return out