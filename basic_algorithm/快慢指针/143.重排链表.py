# @before-stub-for-debug-begin
from python3problem143 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        结合中间节点和反转链表，将单链表拆成两个链表然后归并

        时间复杂度：
        空间复杂度：
        """
        
# @lc code=end

