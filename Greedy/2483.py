"""
2483. Minimum Penalty for a Shop  [Medium]

Approach (prefix/suffix counts):
  - If the shop closes at hour i: penalty = 'N' hours while open (before i)
    + 'Y' hours after closing (from i onward).
  - Start with closing at hour 0 (penalty = all Y's) and sweep forward,
    updating the counts as each hour moves from "after close" to "open".
  - Return the earliest hour with the lowest penalty.

Complexity: O(n) time, O(1) space
"""

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        county = customers.count('Y')  # 'Y' hours at or after the closing time
        countn = 0                     # 'N' hours before the closing time
        penalty, out = county, 0       # best penalty so far and its closing hour

        for i in range(len(customers)):
            # Hour i is now inside the open period
            if customers[i] == 'Y':
                county -= 1  # a customer is served, no longer a penalty
            else:
                countn += 1  # open with no customers: penalty
            temp = county + countn  # penalty if we close at hour i + 1

            if temp < penalty:
                penalty = temp
                out = i + 1

        return out
