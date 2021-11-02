"""
347. Top K Frequent Elements
문제 링크 https://leetcode.com/problems/top-k-frequent-elements/

비어있지 않은 정수 배열이 주어질 때, 가장 많이 등장하는 k개의 원소를 반환하라.
"""

"""
Runtime: 104 ms
Memory Usage: 18.8 MB
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [el[0] for el in Counter(nums).most_common(k)]