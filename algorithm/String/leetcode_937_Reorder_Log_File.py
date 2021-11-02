"""
leetcode 937. Reorder Log File
문제 링크 https://leetcode.com/problems/reorder-data-in-log-files/
"""
"""
Runtime: 60 ms  
Memory Usage: 14.4 MB
"""

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_list = []
        let_list = []
        for log in logs:
            dig_list.append(log) if log.split()[1].isdigit() else let_list.append(log)

        let_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return let_list + dig_list