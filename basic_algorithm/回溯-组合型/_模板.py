class Template:
    def backtracking_combine():
        """
        组合型回溯：
        从n个数中选k个数的 **组合** 可以看成是 **长度固定的子集**
        组合问题可以做一些额外的优化（**剪枝**）

        设path长为m，那么还需要选d=k-m个数
        设当前还需要从[1,i]这i个数中选数
        如果i<d，最后必然无法选出k个数，不需要继续递归
        
        时间复杂度为O(kC^k_n)，叶子的个数乘上根到叶子的路径长度
        空间复杂度为O(n)
        """
        ans = []
        path = []
        def dfs(i):
            # 剪枝
            d = k - len(path)
            if i < d:
                return
            # 边界条件
            if len(path) == k:
                ans.append(path.copy())
                return 
            # 非边界条件
            for j in range(i,0,-1): # 倒序枚举
                path.append(j)
                dfs(j-1)
                path.pop()
        dfs(n)
        return ans
    