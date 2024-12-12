#
# @lc app=leetcode.cn id=1669 lang=python3
#
# [1669] 合并两个链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        """
        要删除从下标a到b到所有节点，即将(a-1)的next指向list2，
        并将list2最后一个节点的next指向(b+1)

        时间复杂度：O(m+n)
        空间复杂度：O(1)
        """
        na = nb = list1
        for _ in range(a-1):
            na = na.next
        for _ in range(b+1):
            nb = nb.next
        na.next = list2
        while na.next:
            na = na.next
        na.next = nb
        return list1
# @lc code=end

