class BuyAndSellII:

	#	Time:	O(n)	|	Space:	O(1)
    def maxProfit(self, prices: List[int]) -> int:
        
        profitTillIndex = 0
        
        #	sum of upslopes only - https://medium.com/algorithms-and-leetcode/best-time-to-buy-sell-stocks-on-leetcode-the-ultimate-guide-ce420259b323
        for i in range(1, len(prices)):
            profitTillIndex = profitTillIndex + ( max(prices[i] - prices[i - 1], 0) )
            
        return profitTillIndex