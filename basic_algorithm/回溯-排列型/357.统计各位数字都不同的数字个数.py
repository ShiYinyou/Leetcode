#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 统计各位数字都不同的数字个数
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        排列型回溯
        """
        if n==0:
            return 1
        ans = []
        path = []
        def dfs(i,s):
            if path:
                ans.append(path.copy())
            if (path and path[0]==0) or len(path) == n:
                return
            for c in s:
                path.append(c)
                dfs(i+1,s-{c})
                path.pop()
        dfs(0,set(range(10)))
        return len(ans)
# @lc code=end

