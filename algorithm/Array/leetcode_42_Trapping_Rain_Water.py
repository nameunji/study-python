"""
leetcode 42. Trapping Rain Water
문제 링크 https://leetcode.com/problems/trapping-rain-water/

음이 아닌 정수의 막대기가 있을 때 막대기 사이에 가둘 수 있는 물의 양을 리턴하라.
"""

"""
방법 1.  
현재 인덱스 위치에서 왼쪽, 오른쪽에서 가장 큰 값을 찾은 후 그 둘 중 작은 값에서 현재 값을 뺀 값을 더해준다.(대신 0보다 커야함)   
Runtime: 1780 ms  
Memory Usage: 14.9 MB
"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        if not height:
            return result

        for i in range(1, len(height)-1):
            left_max = max(height[:i])
            right_max = max(height[i+1:])

            if min(left_max, right_max) - height[i] > 0:
                result += min(left_max, right_max) - height[i]

        return result


"""
코드 2
two pointer를 이용한 풀이 방법이다. 맥락상 위와 비슷하지만, 일일이 해당 시점의 left, right 영역의 max를 구하는 것이 아니라, max를 업데이트하는 방법으로 바꾸었다.  
Runtime: 52 ms  
Memory Usage: 14.8 MB
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        if not height:
            return result

        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        while left < right:
            # 기존에 있던 max값과 현재값을 비교하여 현재값이 크다면 업데이트된다. 아니면 그대로.
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max <= right_max:
                result += left_max - height[left]
                left += 1
            else:
                result += right_max - height[right]
                right -= 1
        return result