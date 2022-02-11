import sys


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_prices = sys.maxsize
        max_profit = 0

        for i in prices:
            if min_prices > i:
                min_prices = i
            cur_profit = i - min_prices
            if cur_profit > max_profit:
                max_profit = cur_profit

        return max_profit


testC = Solution()
if testC.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5:
    print('test1 - Success')
else:
    print('test1 - Fail')

if testC.maxProfit(prices=[7, 6, 4, 3, 1]) == 0:
    print('test2 - Success')
else:
    print('test2 - Fail')

if testC.maxProfit(prices=[2, 4, 0]) == 2:
    print('test3 - Success')
else:
    print('test3 - Fail')
