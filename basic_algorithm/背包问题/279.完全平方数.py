#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        f = [0] + [inf]*n
        for x in range(n+1):
            for c in range(x*x,n+1):
                f[c] = min(f[c],f[c-x*x]+1)
        return f[-1]
# @lc code=end

