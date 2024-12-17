#
# @lc app=leetcode.cn id=1080 lang=python3
#
# [1080] 根到叶路径上的不足节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        """
        对于每个节点，判断其左右子树的最大路径和是否达到limit，
        如果没有，将该子树置为空

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        def f(root,s,limit):
            s += root.val
            if root.left == root.right:
                return s
            mx = -inf
            if root.left:
                x = f(root.left,s,limit)
                mx = max(mx,x)
                if x < limit:
                    root.left = None
            if root.right:
                x = f(root.right,s,limit)
                mx = max(mx,x)
                if x < limit:
                    root.right = None
            return mx
        return None if f(root,0,limit)<limit else root
# @lc code=end

