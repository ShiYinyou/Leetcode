#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = -inf
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        中序遍历
        由于第一个点一定不会是结果，让初始的pre为-inf

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if root is None:
            return inf
        ans = self.getMinimumDifference(root.left)
        ans = min(ans, root.val-self.pre)
        self.pre = root.val
        return min(ans, self.getMinimumDifference(root.right))
# @lc code=end

