#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        完全背包问题的变形
        """
        ### 1. 两个数组
        # n = len(coins)
        # f = [[inf]*(amount+1) for _ in range(2)]
        # f[0][0] = 0
        # for i,x in enumerate(coins):
        #     for j in range(amount+1):
        #         if j<x:
        #             f[(i+1)%2][j] = f[i%2][j]
        #         else:
        #             f[(i+1)%2][j] = min(f[i%2][j],f[(i+1)%2][j-x]+1)
        # return f[n%2][amount] if f[n%2][amount]!=inf else -1

        ### 2. 一个数组
        n = len(coins)
        f = [inf]*(amount+1)
        f[0] = 0
        for x in coins:
            for j in range(x,amount+1):
                f[j] = min(f[j],f[j-x]+1)
        return f[amount] if f[amount]!=inf else -1
    
# @lc code=end

