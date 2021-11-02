"""
leetcode 242. Valid Anagram
문제 링크 https://leetcode.com/problems/valid-anagram/
"""

"""
Runtime: 48 ms
Memory Usage: 15.1 MB
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


"""
Runtime: 40 ms
Memory Usage: 14.4 MB
"""
from collections import Counter

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return dict(Counter(s)) == dict(Counter(t))