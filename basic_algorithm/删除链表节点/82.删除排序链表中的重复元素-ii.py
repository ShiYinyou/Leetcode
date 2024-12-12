#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        与 83 相比，重复的所有节点都要删除
        头节点可能被删除，需要定义一个dummynode

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if head == None:
            return head
        pre = dummy = ListNode(next=head)
        cur = head
        while cur and cur.next:
            val = cur.val
            if val == cur.next.val:
                while cur.next and val == cur.next.val:
                    cur.next = cur.next.next
                pre.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                pre = pre.next
        return dummy.next
# @lc code=end

