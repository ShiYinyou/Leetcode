#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        维护一个控制变量，根据控制变量决定是否翻转结果

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if root is None:
            return []
        ans = []
        q = deque([root])
        rsv = 0
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if rsv:
                vals = vals[::-1]
            ans.append(vals)
            rsv = 1-rsv
        return ans
# @lc code=end

