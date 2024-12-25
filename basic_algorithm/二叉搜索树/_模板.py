class Template:
    def BST(root,target):
        """
        二叉搜索树，在二叉树的基础上，
        要求根节点的左子树所有节点小于根节点，右子树所有节点大于根节点
        同时保证左右子树均为二叉搜索树，符合递归的定义

        验证二叉搜索树的时间复杂度为O(n)，每个节点都遍历了一次
        
        使用二叉搜索树进行搜索的平均时间复杂度为O(lgn)，最坏情况（链）情况下为O(n)
        """
        if target < root.val:
            return BST(root.left, target)
        elif target > root.val:
            return BST(root.right, target)
        else:
            return root

