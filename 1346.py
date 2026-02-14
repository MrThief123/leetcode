'''
1346. Check If N and Its Double Exist
Use a hashmap to store the elements of the array. For each element, check if its double
or half (if it's even) exists in the hashmap. If it does, return True. 
If we finish checking all elements without finding such a pair, return False.
'''

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mydict = {}

        for i in arr:
            if 2*i in mydict or (i%2 == 0 and i//2 in mydict):
                return True
            mydict[i]= True
        return False