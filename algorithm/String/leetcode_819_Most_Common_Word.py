"""
leetcode 819. Most Common Word
문제 링크 https://leetcode.com/problems/most-common-word/
"""

"""
Runtime: 36 ms  
Memory Usage: 14.4 MB
"""
import re
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph_list = re.findall("[A-Za-z]+", paragraph)
        count_list = Counter(paragraph_list).most_common()
        for word, count in count_list:
            if word not in banned:
                return word
