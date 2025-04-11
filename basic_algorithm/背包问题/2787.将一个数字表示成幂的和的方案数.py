#
# @lc app=leetcode.cn id=2787 lang=python3
#
# [2787] 将一个数字表示成幂的和的方案数
#

# @lc code=start
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MAX = 10**9+7
        f = [1] + [0]*n
        for num in range(1,n+1):
            for c in range(n,num**x-1,-1):
                f[c] = f[c] + f[c-num**x]
        print(f)
        return f[-1]%MAX
# @lc code=end

# 4\n1
# 213\n1