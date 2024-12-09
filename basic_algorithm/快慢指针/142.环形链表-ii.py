#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        在 141 的基础上，找到相遇节点后，
        慢指针和头指针继续向前走，一定会在环的入口相遇

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        fast = slow = head
        flag = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True
                break
        if not flag:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head


# @lc code=end

