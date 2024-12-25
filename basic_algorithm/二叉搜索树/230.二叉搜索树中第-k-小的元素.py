# @before-stub-for-debug-begin
from python3problem230 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第 K 小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cnt = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        中序遍历，计数器计数

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if root is None:
            return -1
        l = self.kthSmallest(root.left,k)
        if l != -1:
            return l
        self.cnt += 1
        if self.cnt == k:
            return root.val
        return self.kthSmallest(root.right,k)

# @lc code=end

