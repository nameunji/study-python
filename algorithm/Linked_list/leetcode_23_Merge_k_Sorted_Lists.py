"""
leetcode 23. Merge k Sorted Lists
문제 링크 https://leetcode.com/problems/merge-k-sorted-lists/

linked list가 담긴 배열 lists가 주어지면 모든 linked list를 정렬된 하나의 linked list로 합쳐 반환하라.
"""
"""
방법 1.
각 linked list에서 원소 하나씩 꺼낸 후 비교해서 가장 작은 값을 result에 연결해준다.
꺼낸 linked list의 val을 next로 바꿔준다.
이 과정을 반복해서 lists에 원소가 없을 때까지 반복.

Time Limit Exceeded
"""
from typing import *
from Linked_list.listnode import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [x for x in lists if x]
        result = head = ListNode()
        while len(lists) != 0:
            check = [[i, x.val] for i, x in enumerate(lists)]
            c = min(check, key=lambda n: n[1])
            head.next = ListNode(c[1])
            head = head.next

            if lists[c[0]].next != None:
                lists[c[0]] = lists[c[0]].next
            else:
                del lists[c[0]]

        return result.next


"""
방법 2.
lists의 모든 원소들을 돌면서 각 linked list의 요소들을 하나의 리스트로 합쳐준다.
정렬된 리스트를 하나씩 연결해준다.

Runtime: 92 ms
Memory Usage: 18.2 MB
"""


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = head = ListNode()
        nodes = []
        for x in lists:
            while x:
                nodes.append(x.val)
                x = x.next

        nodes.sort()
        for x in nodes:
            head.next = ListNode(x)
            head = head.next

        return result.next