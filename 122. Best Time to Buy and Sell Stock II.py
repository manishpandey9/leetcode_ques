class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        One of the simplest way is using DP considering all possibilities at every hop
        But that would be not very wise solution as It will take too much time
        So now let's think in terms of greedy solution
        so let say we have list like this [7,1,5,3,6,4], you want to buy at local minima \/ and sell at
        local maxima /\, so basically just traverse the list from start thiking a buy if you get continious
        smaller element keep changing the buy and choose buy as smallest once you
        start getting large elelments keep traversing and find the largest element to sell.
        No need to sell and buy on same day, that does not make sense, we already proved it
        """
        total_profits = 0
        buy_stock = prices[0]
        sell_stock = prices[0]

        for i in range(len(prices)):
            if prices[i] < buy_stock:
                buy_stock = prices[i]
                sell_stock = prices[i]
            elif prices[i] >= sell_stock:
                sell_stock = prices[i]
                if i == len(prices) - 1:
                    total_profits = total_profits + sell_stock - buy_stock
                    return total_profits
                if prices[i+1] < prices[i]:
                    total_profits = total_profits + sell_stock - buy_stock
                    sell_stock = prices[i+1]
                    buy_stock = prices[i+1]

        return total_profits
