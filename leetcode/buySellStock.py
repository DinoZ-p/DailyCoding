"""
Docstring for leetcode.buySellStock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]
        i = 1
        while i < len(prices):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
            i+=1
        return max_profit

            
"""
the core constrain here is that you cannot sell before buy.
one slow approach is that use nested loop to find the max profit pair
and since we cannot sell before buy so we add constrain that j need to be > than i
which we can define the nested loop condtion be j = i+1
the problem is that since it is nested loop, it will find the max profit eventually
but it will take O(n^2) time which is slow

the O(n) approach is that we scan whole arry to find out the min price we could place buy
since profit is always equal to the one of the rest days price - buy price
we can use max() to find the maxprofit by compare current max profit and if we sell on i day price
this also gurantee that sell is always after the buy day.
We don’t scan once to find the global minimum first.
We update the minimum dynamically while scanning.

"""
