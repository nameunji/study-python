"""
771. Jewels and Stones
문제 링크 https://leetcode.com/problems/jewels-and-stones/

J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까?
대소문자는 구분한다.
"""

"""
Runtime: 24 ms
Memory Usage: 14.3 MB
"""

from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        result = 0
        for s in jewels:
            result += counter[s]
        return result