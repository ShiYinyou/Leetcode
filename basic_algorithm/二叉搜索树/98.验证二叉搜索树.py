#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    验证二叉搜索树，要求根节点左边都小于根，右边都大于根
    有前中后序三种写法
    """
    # def isValidBST(self, root: Optional[TreeNode], mn=-inf, mx=inf) -> bool:
    #     """
    #     前序遍历：
    #     对于每个节点，给定一个可以选值的范围，
    #     若在范围内，则返回True

    #     时间复杂度：O(n)
    #     空间复杂度：O(n)
    #     """
    #     if root is None:
    #         return True
    #     if mn < root.val < mx:
    #         return self.isValidBST(root.left,mn,root.val) and self.isValidBST(root.right,root.val,mx)
    #     return False
        
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        中序遍历：
        中序遍历的结果是递增的，只需要判断上一个节点是否比下一个节点小即可
        具体来说：
        当节点为空时，返回True
        递归左子树，如果左子树不是BST，直接返回False
        若当前节点小于等于上一个节点，返回False
        否则记录节点，然后遍历右子树

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     """
    #     后序遍历：
    #     将左右子树的最大最小值传递给根，比较是否满足定义

    #     时间复杂度：O(n)
    #     空间复杂度：O(n)
    #     """
    #     pass
        
# @lc code=end

