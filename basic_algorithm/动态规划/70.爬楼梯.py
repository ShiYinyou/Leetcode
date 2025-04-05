#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        动态规划-记忆化搜索
        设到i层有dfs(i)种方法，则有dfs(i)=dfs(i-1)+dfs(i-2)
        """
        ### 1. 记忆化搜索
        # @cache
        # def dfs(i):
        #     if i==1:
        #         return 1
        #     if i==2:
        #         return 2
        #     return dfs(i-1) + dfs(i-2)
        # return dfs(n)

        ### 2. 递推
        if n==1:
            return 1
        f0, f1 = 1,2
        for i in range(n-2):
            f0,f1 = f1,f0+f1
        return f1
# @lc code=end

