"""
leetcode 973. K Closest Points to Origin
문제 링크 https://leetcode.com/problems/k-closest-points-to-origin/

"""

"""
Runtime: 652 ms
Memory Usage: 19.6 MB
"""

from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        return points[:k]