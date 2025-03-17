#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        组合型回溯
        """
        ans = []
        path = []
        def dfs(i,target):
            d = k-len(path)
            if i < d: # 剩下的数不足
                return
            if len(path)==k and target==0:
                ans.append(path.copy())
                return
            for j in range(i,0,-1):
                path.append(j)
                dfs(j-1,target-j)
                path.pop()
        dfs(9,n)
        return ans
# @lc code=end

