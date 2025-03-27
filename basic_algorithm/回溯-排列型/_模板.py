class Template:
    def backtracking_permute(nums):
        """
        排列型回溯：
        从n个数中选k个数的 **全排列** 可以看成是 **长度固定的子集**

        排列问题不同于组合问题，和顺序是有关的
        每次选择一个节点后，需要修改接下来可选节点的范围
        
        适合从答案角度（选哪个）解决，不适合从选与不选角度解决
        """
        n = len(nums)
        ans = []
        path = [0]*n
        def dfs(i,s):
            if  i == n:
                ans.append(path.copy())
                return 
            # 非边界条件
            for x in s:
                path[i] = x
                dfs(i+1,s-{x})
        dfs(0,set(nums))
        return ans
    