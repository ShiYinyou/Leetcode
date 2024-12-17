#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        对于每个节点，左右子树翻转后交换

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if root:
            root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root
# @lc code=end

