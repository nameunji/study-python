"""
leetcode 125. Valid Palindrome
문제 링크 https://leetcode.com/problems/valid-palindrome/
"""
"""
방법 1.
Runtime: 36 ms  
Memory Usage: 14.9 MB
"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = re.findall("[A-Za-z0-9]", s)
        after = ''.join(word).lower()
        return after == after[::-1]


"""
방법 2.
Runtime: 12 ms
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        return s == s[::-1]