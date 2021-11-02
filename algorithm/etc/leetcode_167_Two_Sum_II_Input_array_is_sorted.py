"""
leetcode 167. Two Sum II - Input array is sorted
문제 링크 https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List

"""
Runtime: 64 ms
Memory Usage: 14.8 MB
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        1. 시작, 끝 인덱스를 지정하여
        2. 두 인덱스의 숫자를 더했을 때 타겟숫자가 되는지 체크한다. (이미 정렬이 되어있기때문에 가능)
        3. if 시작+끝 > 타겟 : 끝 -1
        4. if 시작+끝 < 타겟 : 시작 +1
        5. if 시작+끝 == 타겟 : 시작, 끝 인덱스에 각각 1씩 더해서 리턴
        """
        start = 0
        end = len(numbers) - 1

        while True:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1