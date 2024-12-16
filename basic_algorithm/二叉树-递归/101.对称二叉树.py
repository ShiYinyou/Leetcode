#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        递归判断左右子树是否对称

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        def f(node1,node2):
            if node1 is None or node2 is None:
                return node1 == node2
            return node1.val==node2.val and f(node1.left,node2.right) and f(node1.right,node2.left)
        return f(root.left,root.right)
# @lc code=end

