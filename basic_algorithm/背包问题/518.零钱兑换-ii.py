#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        f = [1] + [0]*(amount)
        for x in coins:
            for c in range(x,amount+1):
                f[c] = f[c] + f[c-x]
        return f[-1]
# @lc code=end

