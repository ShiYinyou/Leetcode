#
# @lc app=leetcode.cn id=2816 lang=python3
#
# [2816] 翻倍以链表形式表示的数字
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        由于存在翻倍后可能存在进位，因此考虑将链表反转后进行操作

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
        dummy = ListNode()
        p0 = dummy
        head = reverseList(head)
        plus = 0
        while head or plus:
            if head:
                s = 2*head.val + plus
            else:
                s = plus
            p0.next = ListNode(s%10)
            plus = s//10
            p0 = p0.next
            if head:
                head = head.next
        return reverseList(dummy.next)
# @lc code=end

