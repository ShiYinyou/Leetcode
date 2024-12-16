class Template:
    def binary_tree_recursion(root):
        """
        二叉树的问题在很多情况下可以被划分成左右子树的两个子问题
        解决子问题和原问题使用的是同一个函数

        递归二叉树的时间复杂度为O(n)，每个节点都遍历了一次
        递归二叉树的空间复杂度为O(n)，使用栈存储，当二叉树是一条链时为O(n)
        """
        left = self.binary_tree_recursion(root.left)
        right = self.binary_tree_recursion(root.right)
        return # 根据需求进行返回

