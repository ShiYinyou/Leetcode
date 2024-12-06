#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        类似 92.反转链表ii
        每k个一组反转，先统计总个数并判断，然后再反转

        时间复杂度：O(n)，虽然有有循环嵌套，但实际上每次都处理了一个节点，最多处理n次
        空间复杂度：O(1)
        """
        dummy = ListNode(next=head)
        p0 = head
        cnt = 0
        while p0:
            cnt += 1
            p0 = p0.next
        p0 = dummy
        pre = None
        cur = p0.next
        while cnt>=k:
            cnt -= k
            for i in range(k):
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

