#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        基于反转链表，反转后进行加和
        一些优化：
        当l1为空而l2非空时，交换l1和l2以保证l1非空，缩减处理l2的重复代码，也不再需要统计长度

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        def reverseList(head):
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        plus = 0
        dummy = ListNode()
        p0 = dummy
        while l1 and l2:
            s = l1.val + l2.val + plus
            p0.next = ListNode(val=s%10)
            plus = s//10
            p0 = p0.next
            l1 = l1.next
            l2 = l2.next
        if l2:
            l1,l2 = l2,l1
        while l1:
            s = l1.val + plus
            p0.next = ListNode(val=s%10)
            plus = s//10
            l1 = l1.next
            p0 = p0.next
        if plus:
            ln = ListNode(1)
            p0.next = ln
        return reverseList(dummy.next)

# @lc code=end

