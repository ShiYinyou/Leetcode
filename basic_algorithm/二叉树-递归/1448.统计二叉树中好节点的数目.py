#
# @lc app=leetcode.cn id=1448 lang=python3
#
# [1448] 统计二叉树中好节点的数目
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        """
        自顶向下，传递根节点到当前节点的最大值

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        ans = 0
        def f(root, mx):
            if root is None:
                return
            if root.val >= mx:
                nonlocal ans
                ans += 1
            mx = max(mx,root.val)
            f(root.left, mx)
            f(root.right, mx)
        f(root, -inf)
        return ans
# @lc code=end

