"""
Leetcode.com #121 - Best Time To Buy and Sell Stock
Easy
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        if not prices:
            return 0
        max_price = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] > max_price:
                max_price = max(max_price, prices[i] - min_price)
        return max_price
        
        maxProf = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1,len(prices)):
                currProfit = prices[j] - prices[i]
                if currProfit > maxProf:
                    maxProf = currProfit
        return maxProf
        """
        maxProf = 0
        currProfit = prices[0]

        for i in range(1,len(prices)):
            minProf = currProfit - prices[i]
            if currProfit > minProf:
                maxProf = currProfit
if __name__ == "__main__":
      sol = Solution()
      prices = [7, 1, 5, 3, 6, 4]
      ans = sol.maxProfit(prices)
      print(f'Prices:{prices}\nAnswer:{ans}')