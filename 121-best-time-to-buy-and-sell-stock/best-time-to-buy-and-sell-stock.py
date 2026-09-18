class Solution(object):
    def maxProfit(self, prices):
        least = prices[0]
        max_price =0
        for price in prices:
            profit = price - least
            if price < least:
                least = price
            elif profit > max_price:
                max_price = profit

        return max_price
     
        