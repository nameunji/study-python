"""
leetcode 104. Maximum Depth of Binary Tree
문제 링크 https://leetcode.com/problems/maximum-depth-of-binary-tree/
Binary tree의 root가 주어지면, 해당 트리의 높이를 반환하라.

Binary tree 이진 트리
자식노드가 최대 두 개인 노드들로 구성된 트리
"""
"""3
Runtime: 40 ms
Memory Usage: 15.3 MB
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        result = 0
        q = deque([root])

        while q:
            result += 1
            for _ in range(len(q)):
                top = q.popleft()
                if top.left is not None:
                    q.append(top.left)
                if top.right is not None:
                    q.append(top.right)

        return result


ex = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
a = Solution()
print(a.maxDepth(ex))