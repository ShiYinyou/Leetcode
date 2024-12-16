#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        类似 104，经典的递归问题
        注意，需要求到根节点的最小深度，如果根只有一颗子树，不能将深度视为1

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if not root:
            return 0
        if root.left and root.right:
            lh = self.minDepth(root.left)
            rh = self.minDepth(root.right)
            return min(lh,rh)+1
        elif root.left:
            return self.minDepth(root.left)+1
        else:
            return self.minDepth(root.right)+1
# @lc code=end

