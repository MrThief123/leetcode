'''
3784. Minimum Deletion Cost to Make All Characters Equal
Use a dictionary to keep track of the total cost for each character.
Then, iterate through the dictionary and calculate the cost of deleting all characters except the one with the highest total cost. 
The answer is the minimum of these costs.
'''

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        from collections import defaultdict
        mydict = defaultdict(int)
        total = 0

        out = float('inf')

        for i in range(len(cost)):
            total += cost[i]
            mydict[s[i]] += cost[i]

        for i in mydict.values():
            out = min(out, total - i)

        return out
