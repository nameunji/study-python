"""
17. Letter Combinations of a Phone Number
문제 링크 https://leetcode.com/problems/letter-combinations-of-a-phone-number/

2에서 9까지 숫자가 주어졌을 때 전화번호로 조합 가능한 모든 문자를 출력하라.
"""

"""
Runtime: 132 ms
Memory Usage: 15.6 MB
"""
from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        result = []

        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)

        dfs(0, "")
        return result


a = Solution()
print(a.letterCombinations('23'))
