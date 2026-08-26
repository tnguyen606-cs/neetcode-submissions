class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Given: 
           prices: prices[i] is the price of NeetCoin on the ith day
           choose a single day to buy, another day to sell
           1 <= prices.length <= 100

        Return:
            max profit or 0

        Approach: Sliding windows
            L, R = prices[0]
            Adding the price the max 
            if the current profit < max:
                move L to the next price

        Time: O(n)
        Space: O(1)
        """

        if len(prices) < 2:
            return 0

        profit = 0
        L, R = 0, 1

        while R < len(prices) and L < R:
            curr = prices[R] - prices[L]
            if curr > 0:
                profit = max(profit, curr)
                R += 1
            else:
                L += 1
                R = L + 1

        return profit

