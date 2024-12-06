#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        要反转一段链表，需要找到前一个节点
        特殊地，当left=1时，需要一个哨兵节点

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        dummy = ListNode(next=head)
        p0 = dummy
        for _ in range(left-1):
            p0 = p0.next
        pre = None
        cur = p0.next
        for i in range(right-left+1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        p0.next.next = cur
        p0.next = pre
        return dummy.next
# @lc code=end

