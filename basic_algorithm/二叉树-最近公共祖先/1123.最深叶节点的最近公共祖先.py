#
# @lc app=leetcode.cn id=1123 lang=python3
#
# [1123] 最深叶节点的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        递归访问左右子树，如果左边高度与右边高度相等，返回当前节点
        否则返回较高的子树节点

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        def f(root):
            if root is None:
                return 0,root
            lh,left = f(root.left)
            rh,right = f(root.right)
            if lh == rh:
                return lh+1,root
            if lh > rh:
                return lh+1,left
            return rh+1,right
        return f(root)[1]
# @lc code=end

