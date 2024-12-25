#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        如果根节点小于区间最小值，向右子树搜索
        如果根节点大于区间最大值，向左子树搜索

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if root is None:
            return 0
        val = root.val
        if val <= low:
            if val == low:
                return self.rangeSumBST(root.right,low,high)+val
            return self.rangeSumBST(root.right,low,high)
        if val >= high:
            if val == high:
                return self.rangeSumBST(root.left,low,high)+val
            return self.rangeSumBST(root.left,low,high)
        return self.rangeSumBST(root.left,low,high)+val+self.rangeSumBST(root.right,low,high)
# @lc code=end

