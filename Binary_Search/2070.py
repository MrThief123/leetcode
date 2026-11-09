'''
2070. Most Beautiful Item for Each Query
1. Create a dictionary to store the maximum beauty for each price.
2. Sort the items by price and create a list of tuples (price, max_beauty) where max_beauty is the maximum beauty for that price.
3. Use binary search to find the maximum beauty for each query by finding the rightmost price that is less than or equal to the query price and returning the corresponding beauty.
4. If no such price exists, return
'''

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        import bisect
        mydict = {}

        for price, beuaty in items:
            if price not in mydict:
                mydict[price] = beuaty
            else:
                mydict[price] = max(mydict[price], beuaty)

        keys = sorted(mydict.keys())

        temp = [(0, 0)]

        for i in keys:
            best = max(temp[-1][1], mydict[i])

            temp.append((i, best))

        out = []

        for i in queries:
            pos = bisect.bisect_right(temp, (i+1,0)) - 1

            out.append(temp[pos][1])

        return out

