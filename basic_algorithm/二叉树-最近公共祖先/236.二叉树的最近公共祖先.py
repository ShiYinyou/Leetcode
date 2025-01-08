#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        判断两个节点分别在当前节点的哪棵子树上
        若都在左子树，则递归左子树
        若都在右子树，则递归右子树
        否则就是当前根节点

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        if left:
            return left
        return right
        
# @lc code=end

