"""
leetcode 232. Implement Queue using Stacks
문제링크 https://leetcode.com/problems/implement-queue-using-stacks/

스택을 이용해 다음 연산을 지원하는 큐를 구현하라
- push : 요소 x를 큐에 삽입
- pop : 큐의 첫 번째 요소를 삭제
- top : 큐의 첫 번째 요소를 조회
- empty : 큐가 비어있는지 여부를 리턴
"""
"""
Runtime: 36 ms
Memory Usage: 14.4 MB
"""
class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return -1

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0