#
# @lc app=leetcode.cn id=1372 lang=python3
#
# [1372] 二叉树中的最长交错路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        对于一个节点，向右的最大值应当等于其右子树向左的最大值+1，或右子树向右的最大值
        向左同理

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        ans = 0
        def f(root,direction):
            nonlocal ans
            if direction == 0:
                if root.left:
                    x = f(root.left,1)+1
                    y = f(root.left,0)
                    ans = max(ans, x, y)
                    return x
                return 0
            if root.right:
                x = f(root.right,0)+1
                y = f(root.right,1)
                ans = max(ans, x, y)
                return x
            return 0
        f(root,0)
        f(root,1)
        return ans
# @lc code=end

