'''
1801. Number of Orders in the Backlog
Use two heaps to maintain the buy and sell orders. For each incoming order, 
try to match it with the opposite heap until it can no longer be matched, then add any remaining amount to the
appropriate heap. Finally, sum up the remaining amounts in both heaps for the answer.
'''

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        import heapq

        buy = []
        sell = []  

        for price, amount, orderType in orders:

            if orderType == 0:  # buy order
                # Try to match with lowest sell orders
                while amount > 0 and sell and sell[0][0] <= price:
                    sell_price, sell_number = heapq.heappop(sell)

                    matched = min(amount, sell_number)
                    amount -= matched
                    sell_number -= matched

                    if sell_number > 0:
                        heapq.heappush(sell, (sell_price, sell_number))

                # leftover buy amount goes to backlog
                if amount > 0:
                    heapq.heappush(buy, (-price, amount))

            else:  # sell order
                # Try to match with highest buy orders
                while amount > 0 and buy and -buy[0][0] >= price:
                    buy_price, buy_number = heapq.heappop(buy)
                    buy_price = -buy_price

                    matched = min(amount, buy_number)
                    amount -= matched
                    buy_number -= matched

                    if buy_number > 0:
                        heapq.heappush(buy, (-buy_price, buy_number))

                # leftover sell amount goes to backlog
                if amount > 0:
                    heapq.heappush(sell, (price, amount))

        MOD = 10**9 + 7
        total = sum(a for _, a in buy) + sum(a for _, a in sell)
        return total % MOD