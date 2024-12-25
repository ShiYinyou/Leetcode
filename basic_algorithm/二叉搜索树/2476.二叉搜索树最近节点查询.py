#
# @lc app=leetcode.cn id=2476 lang=python3
#
# [2476] 二叉搜索树最近节点查询
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        """
        中序遍历得到递增数组，然后二分查找

        时间复杂度：O(m+nlgm)
        空间复杂度：O(m)
        """
        arr = []
        def f(root):
            if root is None:
                return
            f(root.left)
            arr.append(root.val)
            f(root.right)
        f(root)

        ans = []
        for query in queries:
            index = bisect_left(arr,query)
            if index == len(arr):
                ans.append([arr[-1],-1])
            elif arr[index] == query:
                ans.append([query,query])
            elif index==0:
                ans.append([-1,arr[0]])
            else:
                ans.append([arr[index-1],arr[index]])
        return ans
# @lc code=end

