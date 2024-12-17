#
# @lc app=leetcode.cn id=1026 lang=python3
#
# [1026] 节点与其祖先之间的最大差值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        每个子节点需要所有祖先的最大值和最小值才能得到与祖先的最大差

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        ans = -1
        def f(root,mx,mn):
            val = root.val
            nonlocal ans
            ans = max(ans,abs(mx-val),abs(mn-val))
            if root.left:
                f(root.left,max(mx,val),min(mn,val))
            if root.right:
                f(root.right,max(mx,val),min(mn,val))
        f(root,root.val,root.val)
        return ans
# @lc code=end

