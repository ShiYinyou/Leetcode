#
# @lc app=leetcode.cn id=2415 lang=python3
#
# [2415] 反转二叉树的奇数层
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        层序遍历，对奇数层进行反转处理
        偶数层将子节点加入队列时，记录子节点的值
        奇数层取出节点后，修改节点的值

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        q = deque([root])
        cur = 0
        rcd = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if cur%2 == 1:
                    node.val = rcd.pop()
                if node.left is not node.right:
                    q.append(node.left)
                    q.append(node.right)
                    if cur%2==0:
                        rcd.append(node.left.val)
                        rcd.append(node.right.val)
            cur += 1
        return root
# @lc code=end

