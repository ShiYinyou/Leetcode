#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
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
        可根据值大小判断在左子树还是右子树，相当于剪枝了

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        x = root.val
        if p.val < x and q.val < x:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val > x and q.val > x:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
# @lc code=end

