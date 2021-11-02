"""
leetcode 01. Two Sum
문제 링크 https://leetcode.com/problems/two-sum/

주어진 리스트에서 두 수를 뽑아 target이 되는 숫자들의 인덱스를 리턴하라.
"""

"""
Runtime: 48 ms  
Memory Usage: 14.3 MB
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c_dic = {}
        i = 0
        for num in nums:
            if target - num in c_dic:
                return [c_dic[target - num], i]
            c_dic[num] = i
            i += 1