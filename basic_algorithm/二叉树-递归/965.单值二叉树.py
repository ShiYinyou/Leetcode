#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        """
        递归判断根节点是否与左右孩子相同

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        val = root.val
        def f(root):
            if root is None:
                return True
            if root.val != val:
                return False
            return f(root.left) and f(root.right)
        return f(root.left) and f(root.right)
# @lc code=end

