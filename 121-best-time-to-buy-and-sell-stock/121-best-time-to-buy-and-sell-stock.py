class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        best = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                best = max(profit, best)
            else:
                left = right
            right+=1
        return best
                        
                