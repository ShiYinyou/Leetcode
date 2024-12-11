#
# @lc app=leetcode.cn id=2130 lang=python3
#
# [2130] 链表最大孪生和
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        结合链表中间节点和反转链表，计算两个链表对应元素之和

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = head2
            head2 = cur
            cur = nxt
        ans = 0
        while head2:
            ans = max(ans, head.val+head2.val)
            head = head.next
            head2 = head2.next
        return ans
# @lc code=end

