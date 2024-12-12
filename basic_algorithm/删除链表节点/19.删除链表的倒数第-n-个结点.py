#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        要删除倒数第n个节点，就需要找到倒数第n+1个节点
        根据快慢指针思想，让快指针先走n，然后快慢指针一起移动，
        当快指针到达最后一个节点时，慢指针正好位于倒数n+1
        头节点可能被删除，需要定义一个dummynode

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        dummy = ListNode(next=head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
# @lc code=end

