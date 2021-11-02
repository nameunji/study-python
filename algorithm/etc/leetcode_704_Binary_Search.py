"""
leetcode 704. Binary Search
문제 링크 https://leetcode.com/problems/binary-search/
"""
from typing import List

"""
Runtime: 252 ms
Memory Usage: 15.6 MB
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1