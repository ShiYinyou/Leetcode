#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        层序遍历，在每一层中，每个节点的next设置为下一个节点，
        最后一个节点的next设置为空

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if root is None:
            return None
        q = deque([root])
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if i==l-1:
                    node.next = None
                else:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
# @lc code=end

