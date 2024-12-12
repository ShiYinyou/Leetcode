#
# @lc app=leetcode.cn id=3217 lang=python3
#
# [3217] 从链表中移除在数组中存在的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """
        类似 203，但是将比较对象换成了列表中的所有数
        使用哈希表简化查询的开销：可以用set、Counter等
        """
        st = set(nums)
        pre = dummy = ListNode(next=head)
        while pre.next:
            if pre.next.val in st:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next
# @lc code=end

