#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        题中没有给出前一个节点。
        由于指出node不是最后一个节点，可以将下一个节点的值赋给当前节点，然后删除下一个节点实现
        
        时间复杂度：O(1)
        空间复杂度：O(1)
        """
        node.val = node.next.val
        node.next = node.next.next
# @lc code=end

