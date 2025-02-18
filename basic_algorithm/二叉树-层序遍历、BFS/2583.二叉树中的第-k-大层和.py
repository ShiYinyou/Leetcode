#
# @lc app=leetcode.cn id=2583 lang=python3
#
# [2583] 二叉树中的第 K 大层和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        """
        层序遍历，将每一层所有节点值相加，最终排序输出第k大

        时间复杂度：O(nlgn)，时间局限于快排
        空间复杂度：O(n)
        """
        q = deque([root])
        ans = []
        while q:
            val = 0
            for _ in range(len(q)):
                node = q.popleft()
                val += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(val)
        if k > len(ans):
            return -1
        ans.sort()
        return ans[-k]
# @lc code=end

