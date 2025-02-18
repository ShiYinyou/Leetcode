class Template:
    def bfs(root):
        """
        层序遍历、BFS：逐层遍历树中元素
        可通过队列实现

        时间复杂度为O(n)
        """
        if root is None:
            return []
        ans = []
        q = deque([root])
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(vals)
        return ans
