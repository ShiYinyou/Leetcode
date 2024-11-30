class Template:
    def reverse_linked_list(head):
        """
        反转链表是将以链表的头尾节点对调
        用一个指针pre指向前一个节点，cur指向当前节点，nxt指向下一个节点
        反转后，从原链表上看，pre指向反转段的末尾，cur指向反转段的下一个节点
        特殊情况需要添加一个哨兵节点

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
