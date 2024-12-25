#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        遍历，统计个数

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        cnt = Counter()
        mx = 0
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            nonlocal mx
            cnt[root.val] += 1
            mx = max(mx,cnt[root.val])
            dfs(root.right)
        dfs(root)
        return [k for k,v in cnt.items() if v==mx]
# @lc code=end

