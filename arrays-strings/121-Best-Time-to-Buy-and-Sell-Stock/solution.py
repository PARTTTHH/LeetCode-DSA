class Solution(object):
    def maxProfit(self, prices):

        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for day in range(len(prices)):
            if min_price > prices[day]:
                min_price = prices[day]

            current_profit = prices[day] - min_price

            if max_profit < current_profit:
                max_profit = current_profit
        
        return max_profit