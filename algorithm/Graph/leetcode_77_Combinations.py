"""
77. Combinations
문제 링크 https://leetcode.com/problems/combinations/

전체 수 n을 입력받아 k개의 조합을 리턴하라.
"""

"""
Runtime: 76 ms
Memory Usage: 15.6 MB
"""
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int):
        tmp = list(range(1, n+1))
        return list(combinations(tmp, k))


a = Solution()
print(a.combine(4, 2))
