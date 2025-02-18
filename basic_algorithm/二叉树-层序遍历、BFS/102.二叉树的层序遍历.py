#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        层序遍历模版题

        时间复杂度：O(n)
        空间复杂度：O(n)，最后一层至多n/2个节点
        """
        if root is None:
            return []
        ans = []
        dq = deque()
        dq.append(root)
        while len(dq)!=0:
            t = []
            for i in range(len(dq)):
                x = dq.popleft()
                t.append(x.val)
                if x.left:
                    dq.append(x.left)
                if x.right:
                    dq.append(x.right)
            ans.append(t)
        return ans
# @lc code=end

