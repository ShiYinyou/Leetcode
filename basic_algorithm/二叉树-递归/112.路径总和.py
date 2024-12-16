#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        判断左右子树是否包含和为targetSum-root.val的路径

        判断节点为叶子节点的优化写法：left is right（二者均为None）

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if not root:
            return False
        if root.left is root.right:
            return targetSum == root.val
        targetSum -= root.val
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
# @lc code=end

