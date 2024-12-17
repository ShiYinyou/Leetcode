#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        """
        递归统计每棵子树和

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        cnt = Counter()
        def f(root):
            if root is None:
                return 0
            x = root.val+f(root.left)+f(root.right)
            cnt[x] += 1
            return x
        f(root)
        mx = max(cnt.values())
        return [x for x in cnt if cnt[x]==mx]
# @lc code=end

