"""
leetcode 206. Reverse Linked List
문제링크 https://leetcode.com/problems/reverse-linked-list/
"""

"""
Runtime: 36 ms
Memory Usage: 15.6 MB
"""
from Linked_list.listnode import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None

        while node:
            next = node.next  # 넘겨줄 값 2->3->4->5
            node.next = prev  # none
            prev = node       # {val:1, next: None}
            node = next

        return prev