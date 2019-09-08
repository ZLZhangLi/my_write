# #01
# prices = list(map(int,input().strip().split(',')))
# fee = int(input())
#
# def maxProfit(prices, fee):
#     cash, hold = 0, -prices[0]
#     for i in range(1, len(prices)):
#         cash = max(cash, hold + prices[i] - fee)
#         hold = max(hold, cash - prices[i])
#     return cash
#
# res = maxProfit(prices,fee)
# print(res)
from fractions import Fraction
n = int(input())
res = 2 - 2 ** (1 - n)
print(str(Fraction(res)))
