"""
leetcode 148. Sort List
문제 링크 https://leetcode.com/problems/sort-list/
"""
from Linked_list.listnode import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # time : n log n
        # memory : 1
        # 1. 중간 찾기 : runner
        harf, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None  # half 위치를 기준으로 연결리스트 관계를 끊음

        # 2. 병합정렬


"""
Runtime: 160 ms
Memory Usage: 30.2 MB
"""
class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        p = head
        arr = []
        while p:
            arr.append(p.val)
            p = p.next

        arr.sort()
        p = head
        for i in range(len(arr)):
            p.val = arr[i]
            p = p.next

        return head