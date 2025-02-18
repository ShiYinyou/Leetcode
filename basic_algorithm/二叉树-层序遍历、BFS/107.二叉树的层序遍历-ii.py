#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        层序遍历模版题，修改一下输出顺序

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if root is None:
            return []
        ans = []
        deq = deque()
        deq.append(root)
        while deq:
            t = []
            for _ in range(len(deq)):
                x = deq.popleft()
                t.append(x.val)
                if x.left:
                    deq.append(x.left)
                if x.right:
                    deq.append(x.right)
            ans.append(t)
        return ans[::-1]

# @lc code=end

