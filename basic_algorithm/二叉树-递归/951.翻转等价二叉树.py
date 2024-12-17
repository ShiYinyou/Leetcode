#
# @lc app=leetcode.cn id=951 lang=python3
#
# [951] 翻转等价二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        递归考虑左右子树翻转和未翻转两种情况

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if root1 is None or root2 is None:
            return root1 == root2
        if root1.val != root2.val:
            return False
        return (self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)) or (self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left))
# @lc code=end

