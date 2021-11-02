"""
leetcode 238. Product of Array Except Self
문제 링크 https://leetcode.com/problems/product-of-array-except-self/

자기 자신을 제외하고 나머지 요소들의 곱들의 리스트를 반환하는데, 나누기 금지, 리턴할 배열을 위한 공간 메모리를 제외하고 추가로 메모리 사용 금지.
"""

"""
Runtime: 232 ms  
Memory Usage: 20.9 MB
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        out = []
        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out