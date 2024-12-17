#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        递归合并对应节点

        时间复杂度：O(min(m,n))
        空间复杂度：O(min(m,n))
        """
        def f(root1,root2):
            if root1 is None and root2 is None:
                return None
            if root1 is None:
                return root2
            if root2 is None:
                return root1
            return TreeNode(val=root1.val+root2.val,left=f(root1.left,root2.left),right=f(root1.right,root2.right))
        return f(root1,root2)
# @lc code=end

