"""
leetcode 215. Kth Largest Element in an Array
문제 링크 https://leetcode.com/problems/kth-largest-element-in-an-array/
정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.
"""
from typing import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


