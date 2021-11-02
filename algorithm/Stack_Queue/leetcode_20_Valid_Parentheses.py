"""
leetcode - 20. Valid Parentheses
문제링크 https://leetcode.com/problems/valid-parentheses/

괄호로 된 입력값이 올바른지 판별하라.
"""
"""
Runtime: 32 ms
Memory Usage: 14.3 MB
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(': ')', '[': ']', '{': '}'}

        for x in s:
            if x in dic:
                stack.append(x)
            elif len(stack) >= 1:
                tmp = stack.pop()
                if dic[tmp] == x:
                    continue
                else:
                    return False
            else:
                return False

        return not stack