#
# @lc app=leetcode.cn id=2266 lang=python3
#
# [2266] 统计打字方案数
#

# @lc code=start
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MAX = 10**9+7
        kb = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        n = len(pressedKeys)
        ### 1. 记忆化搜索
        # @cache
        # def dfs(i):
        #     if i==n:
        #         return 1
        #     ans = dfs(i+1)
        #     x = pressedKeys[i]
        #     if i+1<n and pressedKeys[i+1] == x:
        #         ans += dfs(i+2)
        #         if i+2<n and pressedKeys[i+2] == x:
        #             ans += dfs(i+3)
        #             if i+3<n and pressedKeys[i+3] == x and (x=="7" or x=="9"):
        #                 ans += dfs(i+4)            
        #     return ans%MAX
        # return dfs(0)

        ### 2. 递推
        dp = [1]+[0]*n
        for i in range(1,n+1):
            x = pressedKeys[i-1]
            dp[i] += dp[i-1]
            if i>=2 and x == pressedKeys[i-2]:
                dp[i] += dp[i-2]
                if i>=3 and x == pressedKeys[i-3]:
                    dp[i] += dp[i-3]
                    if i>=4 and x == pressedKeys[i-4] and (x=="7" or x=="9"):
                        dp[i] += dp[i-4]
            dp[i] %= MAX
        return dp[n]
# @lc code=end

# "222222222222222222222222222222222222"
# "355577777788899"
