#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        自顶向下，将当前得到的数传给下面的节点，通过全局变量计算总和

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        ans = 0
        def f(root, num):
            num = 10*num+root.val
            if root.left is root.right:
                nonlocal ans
                ans += num
                return
            if root.left:
                f(root.left, num)
            if root.right:
                f(root.right, num)
        f(root, 0)
        return ans
# @lc code=end

