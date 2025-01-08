class Template:
    def lowestCommonAncestor(root, p, q):
        """
        如果当前节点为空，或者是p或q，返回当前节点
        判断两个节点分别在当前节点的哪棵子树上
        若都在左子树，则递归左子树
        若都在右子树，则递归右子树
        否则就是当前根节点

        时空复杂度均为O(n)
        """
        if root is None or root is p or root is q:
            return root
        left = lowestCommonAncestor(root.left,p,q)
        right = lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        if left:
            return left
        return right