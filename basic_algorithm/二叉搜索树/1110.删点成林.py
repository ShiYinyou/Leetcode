#
# @lc app=leetcode.cn id=1110 lang=python3
#
# [1110] 删点成林
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
        找到需要删除的节点后，将左右子树加入返回列表，并将该节点置为空

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        ans = []
        s = set(to_delete)
        def f(root):
            if root is None:
                return None
            root.left = f(root.left)
            root.right = f(root.right)
            if root.val in s:
                if root.left:
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
                return None
            return root
        if f(root):
            ans.append(root)
        return [t for t in ans if t is not None]
# @lc code=end

