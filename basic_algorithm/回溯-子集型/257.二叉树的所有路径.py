#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        回溯，遍历每层的每个节点
        """
        ans = []
        path = [str(root.val)]
        def dfs(root):
            if root.left is root.right:
                ans.append("->".join(path))
            if root.left:
                path.append(str(root.left.val))
                dfs(root.left)
                path.pop()
            if root.right:
                path.append(str(root.right.val))
                dfs(root.right)
                path.pop()
        dfs(root)
        return ans
# @lc code=end

