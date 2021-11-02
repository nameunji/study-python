"""
leetcode 49. Group Anagrams
문제 링크 https://leetcode.com/problems/group-anagrams/
"""

"""
Runtime: 96 ms  
Memory Usage: 17 MB
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in ana_dict:
                ana_dict[key] = []
            ana_dict[key].append(word)

        return [x for x in ana_dict.values()]