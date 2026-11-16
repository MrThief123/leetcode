"""
2070. Most Beautiful Item for Each Query  [Medium]

Approach (prefix max + binary search):
  - Keep the best beauty per price, then sort by price.
  - Build a running maximum so each entry holds the best beauty at that price or cheaper.
  - For each query, bisect to the last price <= query and read its running max.
  - A sentinel (0, 0) entry handles queries below every price.

Complexity: O((n + q) log n) time, O(n) space
"""

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        import bisect
        mydict = {}  # price -> best beauty at that exact price

        for price, beuaty in items:
            if price not in mydict:
                mydict[price] = beuaty
            else:
                mydict[price] = max(mydict[price], beuaty)

        keys = sorted(mydict.keys())

        temp = [(0, 0)]  # (price, best beauty with price <= this); sentinel first

        for i in keys:
            best = max(temp[-1][1], mydict[i])

            temp.append((i, best))

        out = []

        for i in queries:
            # Last entry with price <= i
            pos = bisect.bisect_right(temp, (i+1,0)) - 1

            out.append(temp[pos][1])

        return out
