class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        if len(prices) == 1:
            return max_profit

        i, j = 0, 1

        while j < len(prices):
            if prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i])
                print(max_profit)
 
            else:
                i = j
            j += 1

        return max_profit
        