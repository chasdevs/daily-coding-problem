'''
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
'''

'''

maximize profit: P
choose single day to buy: b
choose single day to sell: s

P = prices[s] - prices[b]

Max possible profit ever: max(prices)
P is 0 if prices[i+n] > prices[i] for all n

Naive:
- For every price p on day d, check every other day, keeping running max profit.
- n^2

What if array were sorted?
- max profit without respecting time is simply sorted[end] - sorted[0]
- how to respect time?
- ?

What can we do in one pass?
- Scan from the left to the right.
- Keep track of the min price and keep track of the biggest diff between the current price and the min


'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 99999999
        max = 0
        for price in prices:
            if price < min: min = price
            elif price > min: max = max(price-min, max)
        return max


s = Solution()
prices = [7,6,4,3,1]
s.maxProfit(prices)