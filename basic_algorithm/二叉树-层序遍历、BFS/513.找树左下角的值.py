#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        层序遍历，记录当前遍历层的第一个值

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        ans = None
        q = deque([root])
        while q:
            flag = True
            for _ in range(len(q)):
                node = q.popleft()
                if flag:
                    ans = node.val
                    flag = False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans

# @lc code=end

