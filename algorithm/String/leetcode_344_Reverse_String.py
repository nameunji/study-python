"""
leetcode 344. Reverse String
문제 링크 https://leetcode.com/problems/reverse-string/
"""

"""
방법 1.
Runtime: 36 ms  
Memory Usage: 14.4 MB
"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


"""
방법 2.
Runtime: 188 ms
Memory Usage: 18.3 MB
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1

        while (i < j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1