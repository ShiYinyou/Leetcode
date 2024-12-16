#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        需要判断每棵子树是否是平衡树
        递归获取左右子树的树高

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        def f(root):
            if root is None:
                return 0
            lh = f(root.left)
            if lh == -1:
                return -1
            rh = f(root.right)
            if rh == -1:
                return -1
            if abs(lh-rh)<=1:
                return max(lh,rh)+1
            return -1
        ans = f(root)
        return True if ans!=-1 else False
        
# @lc code=end

