"""
46. Permutations
문제 링크 https://leetcode.com/problems/permutations/

서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.
"""

"""
Runtime: 36 ms
Memory Usage: 14.2 MB
"""
from typing import *
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]):
        return list(permutations(nums))





class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []

        n = len(nums)
        List = []
        temp = [0] * n

        def permute_recursive(nums, index, n):
            if index == n:
                List.append(temp[:])
                return
            for i in range(len(nums)):
                temp[index] = nums[i]
                permute_recursive(nums[:i] + nums[i + 1:], index + 1, n)

        permute_recursive(nums, 0, n)
        return List


a = Solution()
print(a.permute([1,2,3]))
