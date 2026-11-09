'''
2483. Minimum Penalty for a Shop
Medium
Count number of Y's and N's to the right and left of each index.
'''

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        county = customers.count('Y')
        countn = 0
        penalty, out = county, 0


        for i in range(len(customers)):
            if customers[i] == 'Y':
                county -= 1
            else: 
                countn += 1
            temp = county + countn

            if temp < penalty:
                penalty = temp
                out = i + 1


        return out
        