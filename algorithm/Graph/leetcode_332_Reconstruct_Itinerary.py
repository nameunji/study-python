"""
leetcode 332. Reconstruct Itinerary
문제 링크 https://leetcode.com/problems/reconstruct-itinerary/

[from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라.
여러 일정이 있는 경우 사전 어휘 순으로 방문한다.
"""
from typing import *
from collections import defaultdict


"""
Runtime: 80 ms
Memory Usage: 14.9 MB

1. 각 출발지를 키로 가지고 도착지를 값으로 가지는 dict를 생성한다.
    key - str, value - list
2. JFK부터 시작해서 

# sort
>>> b = [['b', 'abb'], ['a', 'abc'], ['b', 'aaa'], ['a', 'aaa']]
>>> c = sorted(b)
>>> c
[['a', 'aaa'], ['a', 'abc'], ['b', 'aaa'], ['b', 'abb']]
"""

class Solution:
    def findItinerary(self, tickets):
        result = []

        graph = defaultdict(list)
        tickets.sort(reverse=True)
        for start, end in tickets:
            graph[start].append(end)

        def dfs(a):
            print(graph)
            while graph[a]:
                dfs(graph[a].pop())
            result.append(a)

        dfs('JFK')
        return result[::-1]


a = Solution()
params = [["JFK","SFO"], ["JFK","ATL"], ["SFO","ATL"], ["ATL","JFK"], ["ATL","SFO"]]
# print(a.findItinerary(params))


class Solution2:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]

# b = Solution2()
# print(b.findItinerary(params))  # ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']

class Solution3:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())

        return stack


c = Solution3()
print(c.findItinerary(params))  # ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
