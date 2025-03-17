#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        组合型回溯
        """
        ans = []
        path = []
        def dfs(i):
            d = k - len(path)
            if i < d: # 剩下的数不足
                return
            if len(path) == k:
                ans.append(path.copy())
                return
            for j in range(i,0,-1): # 倒序枚举
                path.append(j)
                dfs(j-1)
                path.pop()
        dfs(n)
        return ans
# @lc code=end

