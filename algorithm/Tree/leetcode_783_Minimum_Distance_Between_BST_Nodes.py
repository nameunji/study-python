"""
leetcode 783. Minimum Distance Between BST Nodes
문제 링크 https://leetcode.com/problems/minimum-distance-between-bst-nodes/
두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import sys


class Solution:
    min_num = sys.maxsize
    pre = -sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.min_num = min(self.min_num, root.val - self.pre)
        self.pre = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.min_num
