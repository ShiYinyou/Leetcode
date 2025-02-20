#
# @lc app=leetcode.cn id=1609 lang=python3
#
# [1609] 奇偶树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """
        层序遍历，判断每层是否满足要求，一旦发现不满足直接退出程序

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        q = deque([root])
        cur = 0
        while q:
            pre = 0
            for i in range(len(q)):
                node = q.popleft()
                val = node.val
                flag = (cur+val)%2
                if i == 0:
                    if flag==1:
                        pre = val
                    else:
                        return False
                else:
                    if flag==1 and ((cur%2==0 and pre < val) or (cur%2==1 and pre>val)):
                        pre = val
                    else:
                        return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            cur += 1
        return True
# @lc code=end

