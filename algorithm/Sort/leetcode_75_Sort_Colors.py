"""
leetcode 75. Sort Colors
문제 링크 https://leetcode.com/problems/sort-colors/

0, 1, 2로만 이루어진 배열의 접근해서 정렬하는 문제로, 내장함수 sort는 사용하지 않고 정렬하라.
"""

"""
Runtime: 32 ms
Memory Usage: 14.3 MB
"""

from typing import List
from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        i = 0
        for x in range(3):
            if x in count:
                for j in range(count[x]):
                    nums[i] = x
                    i += 1