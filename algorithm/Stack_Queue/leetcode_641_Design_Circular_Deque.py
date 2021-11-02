"""
leetcode - 641. Design Circular Deque
문제링크 https://leetcode.com/problems/design-circular-deque/

Design your implementation of the circular double-ended queue (deque).
"""

"""
방법 1. 배열로 구현

Runtime: 68 ms
Memory Usage: 14.7 MB
"""
from typing import *

class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.q = []

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.q.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.q.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.q.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.q.pop()
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            return self.q[0]
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.q[-1]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return len(self.q) == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.q) == self.k



"""
방법 2. 이중연결리스트로 구현
"""


class Node:
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.left = left
        self.right = right


class MyCircularDeque2:
    def __init__(self, k: int):
        self.k = k
        self.cur = 0
        self.head, self.tail = Node(), Node()
        self.head.right = self.tail  # head -> tail 연결 (doubly linked list)
        self.tail.left = self.head

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            new = Node(value)
            head_left = self.head
            self.head = 0
            self.cur += 1
            return True

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            pass

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            pass

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            pass

    def getFront(self) -> int:
        pass

    def getRear(self) -> int:
        pass

    def isEmpty(self) -> bool:
        return self.cur == 0

    def isFull(self) -> bool:
        return self.cur == self.k