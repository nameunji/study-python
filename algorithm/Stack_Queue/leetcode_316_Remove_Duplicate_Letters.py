"""
leetcode 316. Remove Duplicate Letters
문제링크 https://leetcode.com/problems/remove-duplicate-letters/
"""
"""
각 알파벳의 마지막 인덱스를 추가한다.
만약 마지막 값이 그 다음에 나오지 않는다면 빼면 안 되고,
만약 다음에 나오더라도, 현재 알파벳이 스택의 마지막 값보다 크다면 빼면 안 된다.

Runtime: 36 ms
Memory Usage: 14.3 MB
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = {c: idx for idx, c in enumerate(s)}
        res = []

        for idx, char in enumerate(s):
            if char not in res:
                while res and idx < d[res[-1]] and char < res[-1]:
                    res.pop()
                res.append(char)

        return ''.join(res)


a = Solution()
print(a.removeDuplicateLetters('cbacdcbc'))