"""
24. Swap Nodes in Pairs
문제 링크 https://leetcode.com/problems/swap-nodes-in-pairs/

연결리스트를 입력받아 페어 단위로 스왑하라.
"""
"""
Runtime: 32 ms
Memory Usage: 14.3 MB
"""
from Linked_list.listnode import ListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        top = head

        while top and top.next != None:  # top이 None이 아니고, top.next != None는 홀수가 아님을 체크.
            tmp = top.val
            top.val = top.next.val
            top.next.val = tmp
            top = top.next.next  # 2칸씩 건너뛴다.

        return head


# 위의 코드와 구현 아이디어는 같으나 좀 더 정리하였다.
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next

        return head