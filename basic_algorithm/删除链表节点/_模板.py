class Template:
    def delete_listnode(pre_node,node):
        """
        删除链表的的元素，需要找到节点的前一个节点
        将目标节点前一个节点的next指向目标节点下一个节点即可

        掌握三种特殊情况：
        1. 不会删除最后一个节点（如237）：将下一节点的值赋给当前节点，然后删除下一节点
        2. 会删除头节点：需要定义dummynode
        3. 删除倒数第n个节点（如19），用快慢指针寻找倒数第n+1个节点
        """
        # pre_node 是 node 的前一个节点
        pre_node.next = node.next

