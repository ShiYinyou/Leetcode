#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        删除的节点可能是第一个，也可能是最后一个，
        因此需要定义dummy，并且需要找前一个节点

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        pre = dummy = ListNode(next=head)
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next
# @lc code=end

