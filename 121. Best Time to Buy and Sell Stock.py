from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        so basically in brute force we got to know O(n2), observation was find maximum in right of element  which means
        maintaining a suffix maximum array so we will start from end and find min
        """
        n = len(prices)
        answer = 0
        prefix_max = prices[n-1]
        while(n):
            index = n - 1
            answer = max(answer, prefix_max-prices[index])
            prefix_max = max(prices[index], prefix_max)
            n-=1

        return answer

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        so basic logic would be which is largest element to the right ok, so we traverse the list from end
        an maintain a variable for the largest element
        """
        n = len(prices)
        i = n - 2
        largest_element = prices[n-1]
        max_profit = 0
        while(i>=0):
            max_profit = max(max_profit, largest_element - prices[i])
            largest_element = max(largest_element, prices[i])
            i-=1
        return max_profit
