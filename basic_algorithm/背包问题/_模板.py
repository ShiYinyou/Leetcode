class Template:
    def backtracking_permute(nums):
        """
        背包问题：
        0-1背包和完全背包都是非常重要的DP模型，
        可以说它们就是【选或不选】思想的代表

        n个物品，每个物品体积为w，价值为v，
        如何选择使得体积不超过capacity，价值最大

        先从回溯开始思考，考虑第i个物品选还是不选
        不选，容量不变；选，容量变小
        由此确定递归参数中的i和c
        对应的子问题就是在剩余容量为c的情况下，
        从前i个物品中能得到的最大价值和
        dfs(i,c) = max(dfs(i-1,c),dfs(i-1,c-w[i])+v[i])
        """
        ### === 01背包以 494.目标和 为模板例题 ===
        # 常见变形：
        # 1. 至多装capacity，求方案数/最大价值和
        # 2. 恰好装capacity，求方案数/最大/最小价值和
        # 3. 至少装capacity，求方案数/最大价值和
        # dfs(i,c) = dfs(i-1,c) + dfs(i-1,c-w[i])+v[i]
        def zero_one_knapsack(capacity, w, v):
            n = len(w)
            ### 1. 记忆化搜索
            # @cache
            # def dfs(i,c):
            #     if i < 0: # 一个物品都没有了
            #         return 0
            #     if c < w[i]: # 物品体积超过背包容量，只能不选
            #         return dfs(i-1, c)
            #     # 否则取个最大值
            #     return max(dfs(i-1,c),dfs(i-1,c-w[i])+v[i])
            # return dfs(n-1, capacity)

            ### 2. 递推：把dfs改成f数组，把递归改成循环
            ## f[i][c] = f[i-1][c] + f[i-1][c-w[i]]
            ## f[i+1][c] = f[i][c] + f[i][c-w[i]]
            # f = [[0]*(capacity+1) for _ in range(n+1)]
            # f[0][0] = 1 # 根据实际情况初始化
            # for i,x in enumerate(w):
            #     for c in range(capacity+1):
            #         if c < x:
            #             f[i+1][c] = f[i][c]
            #         else:
            #             f[i+1][c] = f[i][c] + f[i][c-x]
            # return f[n][capacity]

            ### 3. 使用两个数组
            ## f[(i+1)%2][c] = f[(i+1)%2][c] + f[(i+1)%2][c-w[i]]
            # f = [[0]*(capacity+1) for _ in range(2)]
            # f[0][0] = 1 # 根据实际情况初始化
            # for i,x in enumerate(w):
            #     for c in range(capacity+1):
            #         if c < x:
            #             f[(i+1)%2][c] = f[i%2][c]
            #         else:
            #             f[(i+1)%2][c] = f[i%2][c] + f[i%2][c-x]
            # return f[n%2][capacity]

            ### 4. 只用一个数组（避免重复，从右到左算）
            f = [0]*(capacity+1)
            f[0] = 1 # 根据实际情况初始化
            # i多余，直接枚举x
            for x in w:
                for c in range(capacity,x-1,-1):
                    # f[c]=f[c]多余，只需要考虑c>x的情况
                    # 如果只枚举到x，就不用在判断c>x了
                    f[c] = f[c] + f[c-x]
            return f[capacity]


        ### === 完全背包以 322.零钱兑换 为模板例题 ===
        # 从n个变成n种
        # 如果选i，不会变成i-1，而仍然是i
        # dfs(i,c) = max(dfs(i-1,c),dfs(i,c-w[i])+v[i])
        # 常见变形：
        # 1. 至多装capacity，求方案数/最大价值和
        # 2. 恰好装capacity，求方案数/最大/最小价值和
        # 3. 至少装capacity，求方案数/最大价值和
        # dfs(i,c) = min(dfs(i-1,c), dfs(i,c-w[i])+v[i])
        def unbounded_knapsack(capacity, w, v):
            n = len(w)
            ### 1~3. 与0-1背包方法一样
            ### 4. 只用一个数组（正序计算就是对的！！！）
            f = [0]*(capacity+1)
            f[0] = 1 # 根据实际情况初始化
            # i多余，直接枚举x
            for x in w:
                for c in range(x, capacity+1):
                    # f[c]=f[c]多余，只需要考虑c>x的情况
                    # 如果只枚举到x，就不用在判断c>x了
                    f[c] = f[c] + f[c-x]
            return f[capacity]

        
        
    