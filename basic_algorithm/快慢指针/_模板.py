class Template:
    def fast_slow_pointers(head):
        """
        快慢指针是使用一快一慢两个指针来遍历数组并解决问题
        常用于解决中间节点、循环链表、恒定差值、寻找倒数第n个指针等问题
        
        快慢指针的时间复杂度为O(n)
        """
        ### 示例，快指针是慢指针的两倍
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
