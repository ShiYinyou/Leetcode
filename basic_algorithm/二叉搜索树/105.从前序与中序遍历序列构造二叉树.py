#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        前序遍历的第一个元素作为根，
        中序遍历到根之前递归建立左子树，之后递归建立右子树

        时间复杂度：O(n^2)
        空间复杂度：O(n^2)
        """
        if len(preorder)==0:
            return None
        x = preorder[0]
        idx = inorder.index(x)
        l = self.buildTree(preorder[1:idx+1],inorder[:idx])
        r = self.buildTree(preorder[idx+1:],inorder[idx+1:])
        return TreeNode(val=x,left=l, right=r)
# @lc code=end

