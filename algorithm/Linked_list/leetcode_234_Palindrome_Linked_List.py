"""
leetcode 234. Palindrome Linked List
문제 링크 https://leetcode.com/problems/palindrome-linked-list/

singly linked list가 주어지면 Palindrome인지 확인하여 맞으면 True, 아니면 False를 리턴하라
"""
"""
방법 1. deque
LinkedList를 deque로 변환작업을 해주어 양 쪽 끝에서 꺼내기 쉽게 만든다. 그 후 노드의 양 끝에서 요소를 꺼냈을 때 값이 같은지 비교한다.

Runtime: 72 ms
Memory Usage: 24.1 MB
"""
from collections import deque
from Linked_list.listnode import ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        queue = deque()

        node = head
        while node is not None:
            queue.append(node.val)
            node = node.next

        while len(queue) > 1:  # 노드개수가 짝수, 홀수와 상관없이 하기 위해
            if queue.popleft() != queue.pop():
                return False
        return True


"""
방법 2. runner
Runtime: 68 ms
Memory Usage: 24.2 MB
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head  # fast, slow 모두 head에서 시작.

        # fast는 2칸씩, slow는 1칸씩 이동
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next  # slow가 중간까지 이동하면서 역순으로 연결리스트 rev를 만들어나간다.

        if fast:  # 짝수, 홀수의 여부에 따라.
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev

"""
홀수일때, [1,2,3,2,1]
fast : ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
slow : ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
rev : ListNode{val: 1, next: None}

fast : ListNode{val: 1, next: None}
slow : ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
rev : ListNode{val: 2, next: ListNode{val: 1, next: None}}

짝수일때 : [1,2,2,1]
fast : ListNode{val: 2, next: ListNode{val: 1, next: None}}
slow : ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
rev : ListNode{val: 1, next: None}

fast : None
slow : ListNode{val: 2, next: ListNode{val: 1, next: None}}
rev : ListNode{val: 2, next: ListNode{val: 1, next: None}}
"""

"""
collections.deque
list와 deque 시간 복잡도 : https://daimhada.tistory.com/56

- doubled ended queue
- 내부적으로 double linked list로 구현되어 있어, 양 끝에 모두 접근이 가능하다.
- 단, deque의 가운데 부분을 찾거나, 중간에 삽입, 제거하는 것은 더 느리다.
"""