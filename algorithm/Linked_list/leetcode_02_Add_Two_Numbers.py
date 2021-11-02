"""
2. Add Two Numbers
문제 링크 https://leetcode.com/problems/add-two-numbers/

역순으로 저장된 연결리스트의 숫자를 더하라.
"""

"""
Runtime: 72 ms
Memory Usage: 14.2 MB
"""
from Linked_list.listnode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = head = ListNode()

        quotient = 0
        while l1 or l2 or quotient:  # 둘 중 하나라도 None이 아니거나 quotient가 0이 아니면 계속 반복
            if l1:
                quotient += l1.val
                l1 = l1.next
            if l2:
                quotient += l2.val
                l2 = l2.next

            quotient, val = divmod(quotient, 10)  # 몫과 나머지를 구하여, 10을 넘으면 1을 그 다음 val에 넘겨주기 위해.
            head.next = ListNode(val)
            head = head.next

        return result.next