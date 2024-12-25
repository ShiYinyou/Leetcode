#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        后序遍历的最后一个元素作为根，
        中序遍历到根之前递归建立左子树，之后递归建立右子树

        时间复杂度：O(n^2)
        空间复杂度：O(n^2)
        """
        if len(postorder)==0:
            return None
        x = postorder[-1]
        idx = inorder.index(x)
        l = self.buildTree(inorder[:idx],postorder[0:idx])
        r = self.buildTree(inorder[idx+1:],postorder[idx:len(postorder)-1])
        return TreeNode(val=x,left=l, right=r)
# @lc code=end

