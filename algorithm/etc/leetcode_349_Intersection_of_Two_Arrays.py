"""
leetcode 349. Intersection of Two Arrays
문제 링크 https://leetcode.com/problems/intersection-of-two-arrays/
"""
from typing import List, Set

"""
Runtime: 44 ms
Memory Usage: 14.3 MB

set을 이용해 중복을 제거하면서 정렬을 함
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> Set[int]:
        return set(nums1).intersection(set(nums2))


class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> Set[int]:
        return set(nums1) & set(nums2)

"""
# binary search
Runtime: 40 ms
Memory Usage: 14.4 MB
"""
import bisect

class Solution3:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2.sort()

        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1)
            # nums2의 i2 인덱스 위치에 있는 요소와 현재 n1이 같은지 체크해서 result에 넣어준다.
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)

        return result