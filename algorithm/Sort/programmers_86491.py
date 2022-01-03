"""
programmers 최소직사각형
문제 링크 https://programmers.co.kr/learn/courses/30/lessons/86491
"""

"""
Runtime: 80 ms
Memory Usage: 16.2 MB
"""

def solution(sizes):
    max_w, max_h = 0, 0
    for x in sizes:
        w, h = max(x), min(x)
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    return max_w * max_h


