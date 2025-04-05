#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        动态规划
        """
        n = len(cost)
        ### 1. 记忆化搜索
        # @cache
        # def dfs(i):
        #     if i == 0 or i==1:
        #         return 0
        #     return min(dfs(i-1)+cost[i-1],dfs(i-2)+cost[i-2])
        # return dfs(n)

        ### 2. 递推
        f0 = f1 = 0
        for i in range(2,n+1):
            f0,f1 = f1,min(f0+cost[i-2],f1+cost[i-1])
        return f1
# @lc code=end

