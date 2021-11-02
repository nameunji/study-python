"""
leetcode 461. Hamming Distance
문제 링크 https://leetcode.com/problems/hamming-distance/

두 정수를 비트로 표현했을 때 비트가 다른 위치의 갯수를 리턴.
"""

"""
Runtime: 28 ms
Memory Usage: 14.2 MB
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')