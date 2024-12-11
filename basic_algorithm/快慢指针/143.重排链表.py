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
        
        结合 876 查找中间节点和反转链表，转化为两个链表后归并

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        head2 = pre
        dummy = ListNode(next = head)
        x = dummy
        while head2:
            x = x.next
            if x == head2:
                break
            nxt = head2.next
            head2.next = x.next
            x.next = head2
            x = x.next
            head2 = nxt
        if x.next != None:
            x.next = None

# @lc code=end

