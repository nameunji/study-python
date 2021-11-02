"""
leetcode 226. Invert Binary Tree
문제 링크 https://leetcode.com/problems/invert-binary-tree/
이진트리를 반전하라.
"""
"""
bfs방식, swap

Runtime: 28 ms
Memory Usage: 14.4 MB
"""
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root