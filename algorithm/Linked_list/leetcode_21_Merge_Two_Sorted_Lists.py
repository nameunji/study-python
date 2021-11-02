"""
21. Merge Two Sorted Lists
문제링크 https://leetcode.com/problems/merge-two-sorted-lists/

정렬되어 있는 두 연결리스트를 합쳐라.
"""

"""
Runtime: 40 ms
Memory Usage: 14.3 MB
"""
from Linked_list.listnode import ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or l2 and l1.val > l2.val:
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1