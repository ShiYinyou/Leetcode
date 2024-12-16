#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        选出每行的最后一个元素，优先遍历右子树
        
        优化：通过比较当前深度和返回数组长度确定是否需要添加到数组中
        
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        ans = []
        def f(root,height):
            if root is None:
                return
            if len(ans) == height:
                ans.append(root.val)
            f(root.right, height+1)
            f(root.left, height+1)
        f(root,0)
        return ans
# @lc code=end

