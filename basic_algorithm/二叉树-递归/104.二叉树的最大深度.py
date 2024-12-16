#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        最大深度等于左右子树最大深度较大+1
        递归求解

        时间复杂度：O(n)，每个节点遍历了一次
        空间复杂度：O(n)
        """
        if not root:
            return 0
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        return max(lh,rh)+1
# @lc code=end

