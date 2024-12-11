#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        结合 876 查找中间节点和反转链表
        然后两个指针同步遍历两段链表

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        head2 = pre
        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
# @lc code=end

