"""
leetcode 121. Best Time to Buy and Sell Stock
문제 링크 https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

가장 큰 수익을 리턴해라.
"""

"""
방법 1.
1. prices의 마지막 전까지 for문을 돌린다.(마지막은 체크할 필요 없으므로)
2. 현재보다 다음에 올 리스트 중의 max price가 현재가보다 높고 result보다 높다면 result 값을 변경한다.  

Time Limit Exceeded  
for문 안에 새로운 배열을 다시 정렬하는 과정이 있어 타임리밋이 난 듯하다.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)-1):
            next_list = sorted(prices[i+1:], reverse=True)
            if prices[i] < next_list[0] and result < next_list[0]-prices[i]:
                result = next_list[0] - prices[i]
        return result


"""
방법 2.
현재가가 min_price보다 작으면 바꿔주고, result와 현재가에서 min_price를 비교해서 큰 값으로 result를 바꿔준다.  
Runtime: 68 ms  
Memory Usage: 15 MB
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = 999999999

        for price in prices:
            if price < min_price:
                min_price = price
            result = max(result, price-min_price)

        return result