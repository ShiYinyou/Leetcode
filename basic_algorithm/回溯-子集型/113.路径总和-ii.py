#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        回溯问题

        时间复杂度：O(n^2)。在O(n)个叶子结点处m，复制长为O(n)的path
        空间复杂度：O(n)
        """
        if root is None:
            return []
        ans = []
        path = []
        def dfs(root,s):
            if root is None:
                return
            path.append(root.val)
            s += root.val
            if root.left == root.right and s == targetSum:
                    ans.append(path.copy())
            else:
                dfs(root.left,s)
                dfs(root.right,s)
            path.pop()
        dfs(root, 0)
        return ans
# @lc code=end

