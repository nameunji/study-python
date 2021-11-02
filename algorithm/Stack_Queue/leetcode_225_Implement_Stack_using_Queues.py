"""
leetcode 225. Implement Stack using Queues
문제링크 https://leetcode.com/problems/implement-stack-using-queues/

큐를 이용해 다음 연산을 지원하는 스택을 구현하라
- push : 요소 x를 스택에 삽입
- pop : 스택의 첫 번째 요소를 삭제
- top : 스택의 첫 번째 요소를 조회
- empty : 스택이 비어있는지 여부를 리턴
"""
"""
코드 1. collections.deque()를 통해 구현
Runtime: 32 ms
Memory Usage: 14.3 MB
"""
import collections


class MyStack:

    def __init__(self):
        self.stack = collections.deque()

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


"""
코드 2. 리스트를 이용해 구현.
Runtime: 36 ms
Memory Usage: 14.3 MB
"""
class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        return -1

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0