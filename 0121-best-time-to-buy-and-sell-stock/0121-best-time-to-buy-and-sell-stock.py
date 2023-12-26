class Solution(object):
    def maxProfit(self, prices):
        mini  = prices[0]
        maxi = 0
        profit = maxi-mini
        for each in prices:
            if each<mini:
                mini = each
                maxi = each
            if each > maxi:
                maxi = each
                profit = max(profit,maxi-mini)
        return profit
                