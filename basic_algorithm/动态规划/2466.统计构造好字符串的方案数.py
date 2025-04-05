#
# @lc app=leetcode.cn id=2466 lang=python3
#
# [2466] 统计构造好字符串的方案数
#

# @lc code=start
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MAX = 10**9+7
        ### 1. 记忆化搜索
        # @cache
        # def dfs(i):
        #     if i>high:
        #         return 0
        #     if i<low:
        #         return (dfs(i+zero)+dfs(i+one))%MAX
        #     return (dfs(i+zero)+dfs(i+one)+1)%MAX
        # return dfs(0)

        ### 2. 递推
        dp = [1] + [0]*high
        for i in range(1,high+1):
            if i-zero>=0:
                dp[i] += dp[i-zero]
            if i-one >= 0:
                dp[i] += dp[i-one]
        return sum(dp[low:])%MAX
# @lc code=end

