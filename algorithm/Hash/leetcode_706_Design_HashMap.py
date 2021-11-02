"""
706. Design HashMap
문제 링크 https://leetcode.com/problems/design-hashmap/

내장 해시테이블을 사용하지 않고 해시맵을 디자인하라.
"""

"""
Runtime: 371 ms
Memory Usage: 39.5 MB
"""


class MyHashMap:
    def __init__(self):
        self.hash_table = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        if -1 < key < 1000001:
            self.hash_table[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if -1 < key < 1000001:
            return self.hash_table[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if -1 < key < 1000001:
            self.hash_table[key] = -1



"""
Runtime: 228 ms
Memory Usage: 17.8 MB
"""
import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap2:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index] is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next

        return -1

    def remove(self, key: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            return

        # 인덱스의 첫번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
