"""
leetcode 543. Diameter of Binary Tree
문제 링크 https://leetcode.com/problems/diameter-of-binary-tree/
이진트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 틀린 코드
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            return max(left, right) + 1

        result = dfs(root)

        return result
