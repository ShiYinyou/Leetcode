#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        25的特殊情况k=2，可以改为使用nxet和next.next判断个数

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        dummy = ListNode(next=head)
        p0 = dummy
        pre = None
        cur = p0.next
        while p0.next and p0.next.next:
            for i in range(2):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            p0.next.next = cur
            t = p0.next
            p0.next = pre
            p0 = t
        return dummy.next
# @lc code=end

