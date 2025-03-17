#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        组合型回溯，剪枝
        """
        ans = []
        path = []
        candidates.sort()
        n = len(candidates)
        def dfs(i,target):
            if target == 0:
                ans.append(path.copy())
                return
            if i==-1 or target<candidates[0]:
                return
            x = candidates[i]
            if x <= target:
                path.append(x)
                dfs(i,target-x)
                path.pop()
            dfs(i-1,target)
        dfs(n-1,target)
        return ans
# @lc code=end

# [2,3,5]\n8
# [2]\n1
# [8,7,4,3]\n11