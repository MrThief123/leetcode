"""
1801. Number of Orders in the Backlog  [Medium]

Approach (two heaps, simulation):
  - Buy backlog: max-heap (store negated prices). Sell backlog: min-heap.
  - A buy matches the cheapest sells at or below its price; a sell matches the
    highest buys at or above its price.
  - Leftover quantity is pushed to the matching backlog.
  - The answer is the total remaining quantity in both heaps, mod 1e9 + 7.

Complexity: O(n log n) time, O(n) space
"""

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        import heapq

        buy = []   # entries (-price, amount): max-heap by price
        sell = []  # entries (price, amount): min-heap by price

        for price, amount, orderType in orders:

            if orderType == 0:  # buy order
                # Try to match with lowest sell orders
                while amount > 0 and sell and sell[0][0] <= price:
                    sell_price, sell_number = heapq.heappop(sell)

                    matched = min(amount, sell_number)
                    amount -= matched
                    sell_number -= matched

                    # Put back whatever part of the sell order is left
                    if sell_number > 0:
                        heapq.heappush(sell, (sell_price, sell_number))

                # leftover buy amount goes to backlog
                if amount > 0:
                    heapq.heappush(buy, (-price, amount))

            else:  # sell order
                # Try to match with highest buy orders
                while amount > 0 and buy and -buy[0][0] >= price:
                    buy_price, buy_number = heapq.heappop(buy)
                    buy_price = -buy_price  # undo the negation

                    matched = min(amount, buy_number)
                    amount -= matched
                    buy_number -= matched

                    # Put back whatever part of the buy order is left
                    if buy_number > 0:
                        heapq.heappush(buy, (-buy_price, buy_number))

                # leftover sell amount goes to backlog
                if amount > 0:
                    heapq.heappush(sell, (price, amount))

        MOD = 10**9 + 7
        total = sum(a for _, a in buy) + sum(a for _, a in sell)
        return total % MOD
