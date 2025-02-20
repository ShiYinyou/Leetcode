#
# @lc app=leetcode.cn id=2641 lang=python3
#
# [2641] 二叉树的堂兄弟节点 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        层序遍历，每层统计子节点和，并将子节点亲兄弟的值加到各自身上

        时间复杂度：O(nlgn)，时间局限于快排
        空间复杂度：O(n)
        """
        q = deque([root])
        cur = root.val
        s = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                node.val = cur-node.val
                if node.left and node.right:
                    q.append(node.left)
                    q.append(node.right)
                    node.left.val += node.right.val
                    node.right.val = node.left.val
                    s += node.left.val
                elif node.left:
                    q.append(node.left)
                    s += node.left.val
                elif node.right:
                    q.append(node.right)
                    s += node.right.val
            cur = s
            s = 0
        return root
# @lc code=end

