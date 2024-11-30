class Template:
    def reverse_linked_list(head):
        """
        反转链表是将以链表的头尾节点对调

        反转链表的时间复杂度为O(n)
        """
        pre = None
        cur = head
        while cur: # 当前节点不为空
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre # 反转后链表的头节点
