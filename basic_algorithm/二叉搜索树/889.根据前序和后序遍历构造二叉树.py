#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        前序遍历到第一个元素为根节点
        第二个元素为子树的根

        时间复杂度：O(n^2)
        空间复杂度：O(n^2)
        """
        leng = len(preorder)
        if leng == 0:
            return None
        if leng == 1:
            return TreeNode(preorder[0])
        idx = postorder.index(preorder[1])+1
        l = self.constructFromPrePost(preorder[1:idx+1],postorder[:idx])
        r = self.constructFromPrePost(preorder[idx+1:],postorder[idx:leng-1])
        return TreeNode(preorder[0],l,r)
# @lc code=end

