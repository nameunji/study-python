"""
leetcode 561. Array Partition I
문제 링크 https://leetcode.com/problems/array-partition-i/

짝수 개의 정수 배열이 주어지면 (a,b)형태로 둘씩 나눈 후 각각 min()을 했을 때 나온 결과값들의 모든 합이 최대가 될 때 그 최대값을 리턴하라.
"""

"""
방법 1.
리스트를 나눴을 때 작은 순서대로 묶어야 min()을 했을 때 큰 값이 나올 수 있다.  
예시 ) min(1,5) = 1 / min(1,2) = 1  
Runtime: 272 ms  
Memory Usage: 17 MB
"""
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result

"""
방법 2.
위와 비슷한 맥락이지만 약간 파이썬스럽게.
"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])