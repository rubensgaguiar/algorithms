class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = 0
        for price in prices:
            if price < min_price:
                min_price = price

            diff = price - min_price
            if diff > max_price:
                max_price = diff 

        return max_price
