#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
                if node.left!=node.right:
                    q.append(node.left)
                    q.append(node.right)
        return root
# @lc code=end

