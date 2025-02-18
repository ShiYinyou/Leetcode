#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        层序遍历，记录每个叶子节点的高度，并返回最小树高

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if root is None:
            return 0
        h = 0
        ans = []
        q = deque([root])
        while q:
            h += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is node.right:
                    ans.append(h)
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return min(ans)
# @lc code=end

