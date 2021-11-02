"""
leetcode 136. Single Number
문제 링크 https://leetcode.com/problems/single-number/

한번만 나타나는 요소 찾기
"""
from typing import List, Set

"""
방법 1. counter를 이용하여 value가 1인 값 찾기.
Runtime: 140 ms
Memory Usage: 16.8 MB
"""
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = Counter(nums)
        for x in check:
            if check[x] == 1:
                return x


"""
방법 2. sort를 하여 index를 두개씩 건너띄면서 검사하기
Runtime: 128 ms
Memory Usage: 16.8 MB
"""
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums), 2):
            if i + 1 < len(nums):
                if nums[i] != nums[i + 1]:
                    return nums[i]
            else:
                return nums[i]


"""
방법 3. bit연산자 (^) 이
Runtime: 120 ms
Memory Usage: 16.7 MB
"""
class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        element = 0
        for num in nums:
            element ^= num
        return element