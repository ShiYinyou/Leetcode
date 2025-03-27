#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        排列型回溯模板题
        """
        n = len(nums)
        ans = []
        path = [0]*n
        def dfs(i,s):
            if  i == n:
                ans.append(path.copy())
                return 
            # 非边界条件
            for x in s:
                path[i] = x
                dfs(i+1,s-{x})
        dfs(0,set(nums))
        return ans
# @lc code=end

